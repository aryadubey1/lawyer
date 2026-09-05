"""
Telegram notification service.
Builds and sends a formatted message to the configured Telegram bot.
"""
import logging
import requests

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """
    Sends formatted contact form submissions to a Telegram chat via bot API.
    Token and chat_id are read from the SiteConfig singleton at send-time
    so admin changes take effect immediately without restart.
    """

    TELEGRAM_API_URL = 'https://api.telegram.org/bot{token}/sendMessage'

    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id

    @classmethod
    def from_site_config(cls):
        """Factory method: create notifier using current SiteConfig values."""
        from apps.core.models.site_config import SiteConfig
        config = SiteConfig.get_solo()
        return cls(
            bot_token=config.telegram_bot_token,
            chat_id=config.telegram_chat_id,
        )

    def build_message(self, submission) -> str:
        """
        Build a Markdown-formatted Telegram message from a ContactSubmission.
        """
        timestamp = submission.created_at.strftime('%d %b %Y, %I:%M %p IST')
        phone_line = f'📞 *Phone:* {submission.phone}\n' if submission.phone else ''

        return (
            f'📩 *New Contact Form Submission*\n'
            f'━━━━━━━━━━━━━━━━━━━━━━\n'
            f'👤 *Name:* {self._escape(submission.name)}\n'
            f'✉️ *Email:* [{self._escape(submission.email)}](mailto:{submission.email})\n'
            f'{phone_line}'
            f'📋 *Subject:* {self._escape(submission.subject)}\n'
            f'━━━━━━━━━━━━━━━━━━━━━━\n'
            f'💬 *Message:*\n{self._escape(submission.message)}\n'
            f'━━━━━━━━━━━━━━━━━━━━━━\n'
            f'🕒 *Received:* {timestamp}\n'
            f'_Reply via the admin panel: /admin/contact/contactsubmission/_'
        )

    @staticmethod
    def _escape(text: str) -> str:
        """Escape Markdown special characters for Telegram MarkdownV1."""
        return str(text).replace('*', '\\*').replace('_', '\\_').replace('`', '\\`')

    def send(self, submission) -> bool:
        """
        POST the formatted message to the Telegram Bot API.
        Returns True on success, False on failure.
        Updates submission.telegram_sent on success.
        """
        if not self.bot_token or not self.chat_id:
            logger.warning(
                'Telegram notification skipped: bot_token or chat_id not configured in SiteConfig.'
            )
            return False

        message = self.build_message(submission)
        url = self.TELEGRAM_API_URL.format(token=self.bot_token)

        try:
            response = requests.post(
                url,
                json={
                    'chat_id': self.chat_id,
                    'text': message,
                    'parse_mode': 'Markdown',
                    'disable_web_page_preview': True,
                },
                timeout=10,
            )
            response.raise_for_status()
            logger.info(f'Telegram notification sent for submission #{submission.pk}')
            return True

        except requests.exceptions.Timeout:
            logger.error(f'Telegram API timeout for submission #{submission.pk}')
        except requests.exceptions.HTTPError as e:
            logger.error(f'Telegram API HTTP error for submission #{submission.pk}: {e}')
        except requests.exceptions.RequestException as e:
            logger.error(f'Telegram API error for submission #{submission.pk}: {e}')

        return False
