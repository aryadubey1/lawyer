"""
AboutPage singleton model.
"""
from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class AboutPage(models.Model):
    """
    Singleton: always pk=1. Contains all about page content.
    """

    # Intro section
    intro_heading = models.CharField(
        max_length=200,
        default='About Subhash Mishra & Associates',
        verbose_name='Intro Heading',
    )
    intro_text = RichTextField(
        verbose_name='Introduction Text',
        help_text='The main introductory paragraph(s) on the about page.',
    )
    intro_image = CloudinaryField(
        'Intro Image',
        blank=True,
        folder='lex_chambers/about/',
        help_text='Large image shown alongside the introduction. Recommended 800×600px.',
    )
    intro_image_alt = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Intro Image Alt Text',
    )

    # Mission / Vision / Ethics
    mission = RichTextField(
        verbose_name='Our Mission',
        blank=True,
    )
    vision = RichTextField(
        verbose_name='Our Vision',
        blank=True,
    )
    ethics = RichTextField(
        verbose_name='Our Ethics / Core Values',
        blank=True,
    )

    # Stats block
    years_experience = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Years of Experience',
    )
    cases_won = models.PositiveIntegerField(
        default=0,
        verbose_name='Cases Won',
    )
    clients_served = models.PositiveIntegerField(
        default=0,
        verbose_name='Clients Served',
    )
    team_size = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Team Size',
    )

    # Meta
    meta_title = models.CharField(max_length=70, blank=True, verbose_name='Meta Title')
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta Description')

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'

    def __str__(self):
        return 'About Page Content'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
