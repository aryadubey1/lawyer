from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'category', 'order')
    list_display_links = ('alt_text',)
    list_editable = ('order', 'category')
    list_filter = ('category',)
    search_fields = ('alt_text', 'caption')
    ordering = ('order',)
