from django.contrib.sitemaps import Sitemap
from .models import Post


class BlogPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Post.objects.filter(is_published=True).order_by('-published_at')

    def lastmod(self, item):
        return item.updated_at

    def location(self, item):
        return item.get_absolute_url()
