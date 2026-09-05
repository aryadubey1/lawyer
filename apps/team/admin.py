"""
Admin for TeamMember.
"""
from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_founder', 'order', 'is_active')
    list_display_links = ('name',)
    list_editable = ('order', 'is_founder', 'is_active')
    list_filter = ('is_founder', 'is_active')
    search_fields = ('name', 'designation', 'bio')
    ordering = ('order',)
