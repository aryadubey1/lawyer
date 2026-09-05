from django.urls import path
from .api_views import ContactCreateAPIView

urlpatterns = [
    path('contact/', ContactCreateAPIView.as_view(), name='api-contact-create'),
]
