"""
DRF API views for Practice Areas.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import PracticeArea
from .serializers import PracticeAreaListSerializer, PracticeAreaDetailSerializer


class PracticeAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API endpoint for practice areas.
    GET /api/v1/practice-areas/
    GET /api/v1/practice-areas/{slug}/
    """
    queryset = PracticeArea.objects.filter(is_active=True).order_by('order')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['slug']
    search_fields = ['title', 'short_description']
    ordering_fields = ['order', 'title']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PracticeAreaDetailSerializer
        return PracticeAreaListSerializer
