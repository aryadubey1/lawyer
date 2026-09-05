from rest_framework.routers import DefaultRouter
from .api_views import ClientLogoViewSet

router = DefaultRouter()
router.register(r'clients', ClientLogoViewSet, basename='client-logo')

urlpatterns = router.urls
