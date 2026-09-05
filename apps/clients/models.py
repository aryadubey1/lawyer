"""
ClientLogo model — logos for the "Trusted By" section.
"""
from django.db import models
from cloudinary.models import CloudinaryField


class ClientLogo(models.Model):
    name = models.CharField(max_length=200, verbose_name='Client / Company Name')
    logo = CloudinaryField(
        'Logo',
        folder='lex_chambers/clients/',
        help_text='Company logo. PNG with transparent background preferred. Recommended: 200×80px.',
    )
    logo_alt = models.CharField(
        max_length=200,
        verbose_name='Logo Alt Text',
        help_text='Describe the logo for screen readers (e.g. "Acme Corp logo").',
    )
    url = models.URLField(
        blank=True,
        verbose_name='Company Website URL',
        help_text='Optional link when the logo is clicked.',
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Display Order')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Client Logo'
        verbose_name_plural = 'Client Logos'

    def __str__(self):
        return self.name
