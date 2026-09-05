"""
Root URL configuration for Subhash Mishra & Associates.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.contrib.flatpages import views as flatpage_views

from apps.blog.sitemaps import BlogPostSitemap
from apps.practice_areas.sitemaps import PracticeAreaSitemap

sitemaps = {
    'blog': BlogPostSitemap,
    'practice_areas': PracticeAreaSitemap,
}

admin.site.site_header = "Subhash Mishra & Associates — Site Management"
admin.site.site_title = "Subhash Mishra & Associates Admin"
admin.site.index_title = "Welcome to Subhash Mishra & Associates Management Panel"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core / Homepage
    path('', include('apps.core.urls')),

    # Content pages
    path('about/', include('apps.about.urls')),
    path('practice-areas/', include('apps.practice_areas.urls')),
    path('team/', include('apps.team.urls')),
    path('blog/', include('apps.blog.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('contact/', include('apps.contact.urls')),

    # DRF API v1
    path('api/v1/', include('api.urls')),

    # CKEditor (file uploads for rich text fields)
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots_txt'),

    # Flat pages (Privacy Policy, Disclaimer, etc.)
    path('pages/', include('django.contrib.flatpages.urls')),
]

# Serve media locally in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
