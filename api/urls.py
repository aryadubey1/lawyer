"""
API v1 URL aggregator.
All app-level api_urls.py are included here under /api/v1/.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('apps.practice_areas.api_urls')),
    path('', include('apps.team.api_urls')),
    path('', include('apps.blog.api_urls')),
    path('', include('apps.gallery.api_urls')),
    path('', include('apps.clients.api_urls')),
    path('', include('apps.contact.api_urls')),
]
