"""
Views for Team app.
"""
from django.views.generic import ListView
from .models import TeamMember


class TeamListView(ListView):
    model = TeamMember
    template_name = 'team/team.html'
    context_object_name = 'team_members'

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True).order_by('order')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['founder'] = TeamMember.objects.filter(is_founder=True, is_active=True).first()
        return ctx
