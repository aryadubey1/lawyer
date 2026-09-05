"""
Homepage models — HeroSlide for the hero carousel.
"""
from django.db import models
from cloudinary.models import CloudinaryField


class HeroSlide(models.Model):
    """
    A single slide in the homepage hero carousel.
    Managed via TabularInline in the admin under Core / Site Configuration.
    """
    image = CloudinaryField(
        'Hero Slide Image',
        folder='lex_chambers/hero/',
        help_text='Recommended size: 1920×1080px. Will be used as full-bleed background.',
    )
    image_alt = models.CharField(
        max_length=200,
        verbose_name='Image Alt Text',
        help_text='Describe the image for screen readers. Required for accessibility.',
    )
    kicker = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Kicker / Eyebrow Text',
        help_text='Small uppercase text above the heading (e.g. "PREMIER LAW FIRM").',
    )
    heading = models.CharField(
        max_length=200,
        verbose_name='Main Heading',
    )
    subheading = models.TextField(
        blank=True,
        verbose_name='Subheading / Description',
        help_text='Short description beneath the main heading.',
    )
    cta_text = models.CharField(
        max_length=80,
        blank=True,
        default='Schedule a Consultation',
        verbose_name='CTA Button Text',
    )
    cta_url = models.CharField(
        max_length=200,
        blank=True,
        default='/contact/',
        verbose_name='CTA Button URL',
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Display Order',
        help_text='Lower numbers appear first.',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
        help_text='Uncheck to hide this slide without deleting it.',
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Hero Slide'
        verbose_name_plural = 'Hero Slides'

    def __str__(self):
        return f'Slide {self.order}: {self.heading[:60]}'
