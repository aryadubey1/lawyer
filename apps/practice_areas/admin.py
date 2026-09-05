"""
Admin for PracticeArea.
"""
from django.contrib import admin
from .models import PracticeArea


@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'is_active')
    list_display_links = ('title',)
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'icon_svg', 'short_description', 'full_description'),
        }),
        ('Hero Image', {
            'fields': ('hero_image', 'hero_image_alt'),
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active'),
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )
