"""
Django Q2 async task: send Telegram notification for a contact submission.
Called via: async_task('apps.contact.tasks.send_telegram_notification', submission_id)
"""
import logging
from apps.contact.services.telegram_service import TelegramNotifier

logger = logging.getLogger(__name__)


def send_telegram_notification(submission_id: int) -> None:
    """
    Fetch the ContactSubmission by ID and send a Telegram notification.
    Updates telegram_sent=True on success.
    Safe to retry — checks existing state.
    """
    from apps.contact.models import ContactSubmission

    try:
        submission = ContactSubmission.objects.get(pk=submission_id)
    except ContactSubmission.DoesNotExist:
        logger.error(f'send_telegram_notification: submission #{submission_id} not found.')
        return

    if submission.telegram_sent:
        logger.info(f'Submission #{submission_id} already notified via Telegram. Skipping.')
        return

    notifier = TelegramNotifier.from_site_config()
    success = notifier.send(submission)

    if success:
        submission.telegram_sent = True
        submission.save(update_fields=['telegram_sent'])
        logger.info(f'Submission #{submission_id} telegram_sent=True saved.')
    else:
        logger.warning(f'Submission #{submission_id} Telegram notification failed.')
