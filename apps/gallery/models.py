"""
GalleryImage model — filterable by category via Alpine.js tabs.
"""
from django.db import models
from cloudinary.models import CloudinaryField


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('justice', 'Justice & Law'),
        ('office', 'Our Office'),
        ('team', 'Our Team'),
        ('event', 'Events'),
    ]

    image = CloudinaryField(
        'Image',
        folder='lex_chambers/gallery/',
        help_text='High-quality photograph. Recommended minimum 800×600px.',
    )
    alt_text = models.CharField(
        max_length=200,
        verbose_name='Alt Text',
        help_text='Describe the image for screen readers. Required.',
    )
    caption = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='Caption',
        help_text='Optional caption shown in the lightbox.',
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='office',
        verbose_name='Category',
        help_text='Used for the filter tabs on the gallery page.',
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Display Order',
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return f'{self.get_category_display()}: {self.alt_text[:60]}'

    @property
    def thumbnail_url(self):
        if not self.image:
            return ''
        return self.image.build_url(
            width=600, height=450, crop='fill',
            gravity='auto', quality='auto', fetch_format='auto'
        )

    @property
    def lightbox_url(self):
        if not self.image:
            return ''
        return self.image.build_url(
            width=1600, crop='limit',
            quality='auto', fetch_format='auto'
        )
