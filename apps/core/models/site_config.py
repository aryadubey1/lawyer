"""
SiteConfig — singleton model holding all firm-wide settings.
Enforces singleton pattern via save() override (always pk=1).
"""
from django.db import models


class SiteConfig(models.Model):
    """
    Singleton model: only one row ever exists (pk=1).
    All site-wide configuration lives here and is injected into every
    template via the site_config_processor context processor.
    """

    # ─── Firm Identity ─────────────────────────────────────────────────────────
    firm_name = models.CharField(
        max_length=200,
        default='Subhash Mishra & Associates',
        verbose_name='Firm Name',
    )
    firm_tagline = models.CharField(
        max_length=300,
        blank=True,
        default='Excellence in Legal Practice',
        verbose_name='Firm Tagline',
    )
    footer_about_text = models.TextField(
        blank=True,
        default=(
            'Subhash Mishra & Associates is a full-service litigation and advisory '
            'chambers committed to principled, strategic, and result-oriented '
            'representation across trial courts, High Courts, and the Supreme Court of India.'
        ),
        verbose_name='Footer About Text',
        help_text='Short description shown in the footer beneath the logo.',
    )

    # ─── Contact Information ────────────────────────────────────────────────────
    phone_primary = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Primary Phone',
    )
    phone_secondary = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Secondary Phone',
        help_text='Optional second phone number.',
    )
    email_primary = models.EmailField(
        blank=True,
        verbose_name='Primary Email',
    )
    office_hours = models.CharField(
        max_length=100,
        blank=True,
        default='Mon–Fri 09:00–20:00',
        verbose_name='Office Hours',
    )

    # ─── Address ───────────────────────────────────────────────────────────────
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name='Address Line 1')
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=100, blank=True, verbose_name='City')
    state = models.CharField(max_length=100, blank=True, verbose_name='State')
    pincode = models.CharField(max_length=10, blank=True, verbose_name='PIN Code')

    google_map_embed_url = models.TextField(
        blank=True,
        verbose_name='Google Map Embed URL',
        help_text=(
            'Paste the src URL from a Google Maps embed code. '
            'Go to Google Maps → Share → Embed a map → copy the src="..." value.'
        ),
    )

    # ─── Social Media ──────────────────────────────────────────────────────────
    facebook_url = models.URLField(blank=True, verbose_name='Facebook URL')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn URL')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter / X URL')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram URL')

    # ─── Telegram Notifications ────────────────────────────────────────────────
    telegram_bot_token = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Telegram Bot Token',
        help_text=(
            'Create a bot via @BotFather on Telegram. '
            'It will provide a token like: 123456789:ABC-defGHI...'
        ),
    )
    telegram_chat_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Telegram Chat ID',
        help_text=(
            '1. Start a conversation with your bot on Telegram. '
            '2. Visit https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates '
            '3. Copy the "chat":{"id": ...} value. '
            'To notify multiple people, separate their chat IDs with a comma '
            '(e.g. 123456789,987654321) — each person must message the bot at least once first.'
        ),
    )

    # ─── Feature Toggles ───────────────────────────────────────────────────────
    show_client_logos_section = models.BooleanField(
        default=True,
        verbose_name='Show "Trusted By" Client Logos Section',
        help_text='Toggle whether the client logos strip appears on the homepage.',
    )

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return f'{self.firm_name} — Site Configuration'

    def save(self, *args, **kwargs):
        """Enforce singleton: always save as pk=1."""
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Prevent deletion of the singleton."""
        pass

    @classmethod
    def get_solo(cls):
        """Retrieve or create the singleton instance."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    @property
    def full_address(self):
        parts = filter(None, [
            self.address_line_1,
            self.address_line_2,
            self.city,
            self.state,
            self.pincode,
        ])
        return ', '.join(parts)

    def _firm_name_parts(self):
        """Split firm_name into a gold lead-in and remainder (e.g. 'Subhash Mishra' / '& Associates')."""
        name = (self.firm_name or '').strip()
        if ' & ' in name:
            lead, rest = name.split(' & ', 1)
            return lead.strip(), f'& {rest.strip()}'
        parts = name.split(None, 1)
        if len(parts) == 2:
            return parts[0], parts[1]
        return name, ''

    @property
    def firm_name_lead(self):
        return self._firm_name_parts()[0]

    @property
    def firm_name_rest(self):
        return self._firm_name_parts()[1]
