"""
Contact form admin — read-mostly, with unread indicator.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('status_badge', 'name', 'email', 'subject', 'created_at', 'telegram_sent', 'is_read')
    list_display_links = ('name',)
    list_editable = ('is_read',)
    list_filter = ('is_read', 'telegram_sent', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    readonly_fields = (
        'name', 'email', 'phone', 'subject', 'message',
        'created_at', 'telegram_sent',
    )

    fieldsets = (
        ('Submission Details', {
            'fields': ('name', 'email', 'phone', 'subject', 'message', 'created_at'),
        }),
        ('Status', {
            'fields': ('is_read', 'telegram_sent'),
        }),
    )

    def has_add_permission(self, request):
        return False

    @admin.display(description='Status')
    def status_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="color: #22c55e; font-size: 1.2em;" title="Read">🟢</span>')
        return format_html('<span style="color: #ef4444; font-size: 1.2em;" title="Unread">🔴</span>')
