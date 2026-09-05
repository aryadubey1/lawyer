"""
Views for Practice Areas app.
"""
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import PracticeArea


class PracticeAreaListView(ListView):
    model = PracticeArea
    template_name = 'practice_areas/list.html'
    context_object_name = 'practice_areas'

    def get_queryset(self):
        return PracticeArea.objects.filter(is_active=True).order_by('order')


class PracticeAreaDetailView(DetailView):
    model = PracticeArea
    template_name = 'practice_areas/detail.html'
    context_object_name = 'practice_area'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return PracticeArea.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Related blog posts
        ctx['related_posts'] = (
            self.object.blog_posts.filter(is_published=True)
            .order_by('-published_at')[:3]
        )
        # Other practice areas for sidebar
        ctx['other_areas'] = (
            PracticeArea.objects.filter(is_active=True)
            .exclude(pk=self.object.pk)
            .order_by('order')
        )
        return ctx
