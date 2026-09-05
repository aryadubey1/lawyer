"""
Blog views — list, detail, category filter.
"""
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Category, Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category').order_by('-published_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        ctx['active_category'] = None
        return ctx


class PostCategoryView(PostListView):
    """Filter posts by category."""

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(
            is_published=True, category=self.category
        ).select_related('category').order_by('-published_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active_category'] = self.category
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category', 'related_practice_area')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Recent posts for sidebar
        ctx['recent_posts'] = (
            Post.objects.filter(is_published=True)
            .exclude(pk=self.object.pk)
            .order_by('-published_at')[:4]
        )
        ctx['categories'] = Category.objects.all()
        return ctx
