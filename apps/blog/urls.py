from django.urls import path
from .views import PostListView, PostDetailView, PostCategoryView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('category/<slug:slug>/', PostCategoryView.as_view(), name='category'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
]
