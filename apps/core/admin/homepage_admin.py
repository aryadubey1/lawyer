"""
Admin configuration for HeroSlide.
"""
from django.contrib import admin
from apps.core.models.homepage import HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    """
    Standalone admin for managing hero carousel slides.
    The lawyer can add/remove/reorder slides directly from this list view.

    Note: HeroSlide has no ForeignKey back to SiteConfig, so it cannot be
    registered as a TabularInline (Django requires that FK relationship for
    inlines to work). Since SiteConfig is a singleton anyway, there's no
    parent instance to nest slides under — a standalone admin with
    list_editable ordering achieves the same "manage everything in one
    screen" goal without that requirement.
    """
    list_display = ('heading', 'kicker', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    fields = ('image', 'image_alt', 'kicker', 'heading', 'subheading', 'cta_text', 'cta_url', 'order', 'is_active')