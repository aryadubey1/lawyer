"""
PracticeArea model — represents a legal practice area offered by the firm.
"""
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class PracticeArea(models.Model):
    """
    A practice area / legal service. Displayed in a 3-column card grid
    on the homepage and as a navigable list+detail.
    """

    # Icon: simple text field for an icon class (e.g. Heroicons SVG name)
    # or you can paste an SVG string directly for max flexibility
    icon_svg = models.TextField(
        blank=True,
        verbose_name='Icon SVG',
        help_text='Paste a Heroicons/FontAwesome SVG code here (line-art style, will be gold-colored via CSS).',
    )

    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name='URL Slug',
        help_text='Auto-generated from title. Used in URLs.',
    )
    short_description = models.TextField(
        max_length=400,
        verbose_name='Short Description',
        help_text='2–3 sentences shown on the homepage card. Keep concise.',
    )
    full_description = RichTextField(
        verbose_name='Full Description',
        help_text='Detailed description for the practice area detail page.',
    )
    hero_image = CloudinaryField(
        'Hero Image',
        blank=True,
        folder='lex_chambers/practice_areas/',
        help_text='Large image for the detail page header. Recommended 1400×600px.',
    )
    hero_image_alt = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Hero Image Alt Text',
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Display Order',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
        help_text='Inactive practice areas are hidden from the site.',
    )

    # SEO
    meta_title = models.CharField(
        max_length=70,
        blank=True,
        verbose_name='Meta Title',
        help_text='SEO title tag. Leave blank to use the practice area title.',
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta Description',
        help_text='SEO meta description. Keep under 160 characters.',
    )

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Practice Area'
        verbose_name_plural = 'Practice Areas'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('practice_areas:detail', kwargs={'slug': self.slug})

    @property
    def effective_meta_title(self):
        if self.meta_title:
            return self.meta_title
        from apps.core.models.site_config import SiteConfig
        return f'{self.title} | {SiteConfig.get_solo().firm_name}'
