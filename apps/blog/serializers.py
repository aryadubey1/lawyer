from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    excerpt = serializers.CharField(source='effective_excerpt', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'category', 'featured_image', 'image_alt', 'excerpt', 'published_at', 'url']


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'category', 'related_practice_area',
            'featured_image', 'image_alt', 'excerpt', 'body',
            'meta_title', 'meta_description', 'published_at', 'url',
        ]
