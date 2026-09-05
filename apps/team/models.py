"""
TeamMember model.
"""
from django.db import models
from cloudinary.models import CloudinaryField


class TeamMember(models.Model):
    name = models.CharField(max_length=200, verbose_name='Full Name')
    designation = models.CharField(
        max_length=200,
        verbose_name='Designation / Title',
        help_text='e.g. "Senior Advocate", "Associate Attorney"',
    )
    bio = models.TextField(
        verbose_name='Biography',
        help_text='Full professional biography.',
    )
    photo = CloudinaryField(
        'Photo',
        blank=True,
        folder='lex_chambers/team/',
        help_text='Professional headshot. Square format recommended (e.g. 400×400px).',
    )
    photo_alt = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Photo Alt Text',
        help_text='Describe the photo for screen readers.',
    )
    is_founder = models.BooleanField(
        default=False,
        verbose_name='Is Founder',
        help_text='The founder is featured prominently on the homepage and about page.',
    )
    linkedin_url = models.URLField(
        blank=True,
        verbose_name='LinkedIn Profile URL',
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Display Order',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
    )

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return f'{self.name} — {self.designation}'
