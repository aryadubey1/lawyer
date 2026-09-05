"""
Admin configuration for SiteConfig singleton.
"""
from django.contrib import admin
from django.shortcuts import redirect
from apps.core.models.site_config import SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    """
    Singleton admin: hides the 'add' button and prevents
    navigation away from the single instance.
    """

    fieldsets = (
        ('Firm Identity', {
            'fields': ('firm_name', 'firm_tagline', 'footer_about_text'),
        }),
        ('Contact Information', {
            'fields': (
                'phone_primary', 'phone_secondary',
                'email_primary', 'office_hours',
            ),
        }),
        ('Office Address', {
            'fields': (
                'address_line_1', 'address_line_2',
                'city', 'state', 'pincode',
                'google_map_embed_url',
            ),
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'linkedin_url', 'twitter_url', 'instagram_url'),
            'classes': ('collapse',),
        }),
        ('Telegram Notifications', {
            'fields': ('telegram_bot_token', 'telegram_chat_id'),
            'description': (
                '<strong>Required for contact form Telegram notifications.</strong> '
                'Create a bot via @BotFather and paste the token here. '
                'Also run <code>python manage.py qcluster</code> for async processing.'
            ),
        }),
        ('Feature Toggles', {
            'fields': ('show_client_logos_section',),
        }),
    )

    def has_add_permission(self, request):
        """Prevent creating a second SiteConfig row."""
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deleting the singleton."""
        return False

    def changelist_view(self, request, extra_context=None):
        """Redirect the changelist directly to the singleton instance."""
        obj = SiteConfig.get_solo()
        return redirect(f'../{obj.pk}/change/')