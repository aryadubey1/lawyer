"""
Blog admin — Category and Post.
"""
from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at', 'created_at')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'related_practice_area')
    search_fields = ('title', 'excerpt', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ('-published_at', '-created_at')

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'category', 'related_practice_area', 'excerpt', 'body'),
        }),
        ('Featured Image', {
            'fields': ('featured_image', 'image_alt'),
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at'),
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
