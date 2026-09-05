"""
Blog Post model.
"""
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    slug = models.SlugField(max_length=320, unique=True, verbose_name='Slug')
    category = models.ForeignKey(
        'blog.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Category',
    )
    related_practice_area = models.ForeignKey(
        'practice_areas.PracticeArea',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts',
        verbose_name='Related Practice Area',
        help_text='Optional link to a practice area for cross-referencing.',
    )
    featured_image = CloudinaryField(
        'Featured Image',
        blank=True,
        folder='lex_chambers/blog/',
        help_text='Recommended size: 1200×630px.',
    )
    image_alt = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Image Alt Text',
    )
    excerpt = models.TextField(
        max_length=400,
        blank=True,
        verbose_name='Excerpt',
        help_text='Short summary shown on list pages. If blank, auto-generated from body.',
    )
    body = RichTextUploadingField(
        verbose_name='Post Body',
        help_text='Full post content with rich text editor.',
    )

    # Publishing
    is_published = models.BooleanField(
        default=False,
        verbose_name='Published',
        help_text='Only published posts are shown on the public site.',
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Published At',
        help_text='Set this to schedule publication. Leave blank to publish immediately.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # SEO
    meta_title = models.CharField(max_length=70, blank=True, verbose_name='Meta Title')
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta Description')

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', kwargs={'slug': self.slug})

    @property
    def effective_excerpt(self):
        if self.excerpt:
            return self.excerpt
        # Strip HTML tags for auto-excerpt
        import re
        clean = re.sub(r'<[^>]+>', '', self.body)
        return clean[:200] + '...' if len(clean) > 200 else clean

    @property
    def effective_meta_title(self):
        if self.meta_title:
            return self.meta_title
        from apps.core.models.site_config import SiteConfig
        return f'{self.title} | {SiteConfig.get_solo().firm_name} Blog'
