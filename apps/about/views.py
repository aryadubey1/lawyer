from django.views.generic import TemplateView
from .models import AboutPage
from apps.team.models import TeamMember


class AboutPageView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['about'] = AboutPage.get_solo()
        ctx['founder'] = TeamMember.objects.filter(is_founder=True, is_active=True).first()
        ctx['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')
        return ctx
