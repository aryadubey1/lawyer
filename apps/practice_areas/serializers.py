"""
DRF Serializers for PracticeArea.
"""
from rest_framework import serializers
from .models import PracticeArea


class PracticeAreaListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views."""
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = PracticeArea
        fields = [
            'id', 'title', 'slug', 'icon_svg',
            'short_description', 'order', 'url',
        ]


class PracticeAreaDetailSerializer(serializers.ModelSerializer):
    """Full serializer for detail views."""
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = PracticeArea
        fields = [
            'id', 'title', 'slug', 'icon_svg',
            'short_description', 'full_description',
            'hero_image', 'hero_image_alt',
            'order', 'meta_title', 'meta_description', 'url',
        ]
