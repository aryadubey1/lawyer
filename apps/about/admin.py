from django.contrib import admin
from .models import AboutPage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Introduction', {
            'fields': ('intro_heading', 'intro_text', 'intro_image', 'intro_image_alt'),
        }),
        ('Mission, Vision & Ethics', {
            'fields': ('mission', 'vision', 'ethics'),
        }),
        ('Statistics Block', {
            'fields': ('years_experience', 'cases_won', 'clients_served', 'team_size'),
            'description': 'These numbers appear in the "Our Achievements" stats strip.',
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        obj, _ = AboutPage.objects.get_or_create(pk=1)
        return redirect(f'/admin/about/aboutpage/{obj.pk}/change/')
