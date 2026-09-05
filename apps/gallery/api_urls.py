from rest_framework.routers import DefaultRouter
from .api_views import GalleryImageViewSet

router = DefaultRouter()
router.register(r'gallery', GalleryImageViewSet, basename='gallery-image')

urlpatterns = router.urls
