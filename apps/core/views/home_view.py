"""
Homepage view — aggregates data from multiple apps for the homepage sections.
"""
from django.views.generic import TemplateView

from apps.core.models.homepage import HeroSlide
from apps.about.models import AboutPage
from apps.practice_areas.models import PracticeArea
from apps.team.models import TeamMember
from apps.blog.models import Post
from apps.gallery.models import GalleryImage
from apps.clients.models import ClientLogo


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Hero carousel slides (active only, ordered)
        ctx['hero_slides'] = HeroSlide.objects.filter(is_active=True).order_by('order')

        # About snapshot
        ctx['about_page'] = AboutPage.get_solo()

        # Practice areas grid (all, ordered)
        ctx['practice_areas'] = PracticeArea.objects.filter(is_active=True).order_by('order')

        # Founder spotlight
        ctx['founder'] = TeamMember.objects.filter(is_founder=True).first()

        # All team members for team section
        ctx['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')

        # Latest 3 published blog posts
        ctx['latest_posts'] = (
            Post.objects.filter(is_published=True)
            .select_related('category')
            .order_by('-published_at')[:3]
        )

        # Gallery images (homepage shows a cross-section — 8 max)
        ctx['gallery_images'] = GalleryImage.objects.all().order_by('order')[:8]

        # Client logos
        ctx['client_logos'] = ClientLogo.objects.all().order_by('order')

        return ctx
