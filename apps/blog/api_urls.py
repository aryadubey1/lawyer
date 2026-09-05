from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register(r'blog/categories', CategoryViewSet, basename='blog-category')
router.register(r'blog/posts', PostViewSet, basename='blog-post')

urlpatterns = router.urls
