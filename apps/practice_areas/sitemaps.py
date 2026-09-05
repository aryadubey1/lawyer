"""
Sitemap for Practice Areas.
"""
from django.contrib.sitemaps import Sitemap
from .models import PracticeArea


class PracticeAreaSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return PracticeArea.objects.filter(is_active=True)

    def location(self, item):
        return item.get_absolute_url()
