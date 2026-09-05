"""
ContactSubmission model.
"""
from django.db import models


class ContactSubmission(models.Model):
    name = models.CharField(max_length=200, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email Address')
    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Phone Number',
        help_text='Optional.',
    )
    subject = models.CharField(max_length=300, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Received At')
    is_read = models.BooleanField(
        default=False,
        verbose_name='Marked as Read',
        help_text='Check this once you have addressed the enquiry.',
    )
    telegram_sent = models.BooleanField(
        default=False,
        verbose_name='Telegram Notification Sent',
        help_text='Set automatically. If False after a minute, the qcluster may not be running.',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'

    def __str__(self):
        return f'{self.name} — {self.subject[:60]} ({self.created_at.strftime("%d %b %Y")})'
