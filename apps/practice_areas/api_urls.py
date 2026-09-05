"""
API URL patterns for Practice Areas.
"""
from rest_framework.routers import DefaultRouter
from .api_views import PracticeAreaViewSet

router = DefaultRouter()
router.register(r'practice-areas', PracticeAreaViewSet, basename='practice-area')

urlpatterns = router.urls
