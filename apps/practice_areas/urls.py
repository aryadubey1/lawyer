"""
URL patterns for Practice Areas app.
"""
from django.urls import path
from .views import PracticeAreaListView, PracticeAreaDetailView

app_name = 'practice_areas'

urlpatterns = [
    path('', PracticeAreaListView.as_view(), name='list'),
    path('<slug:slug>/', PracticeAreaDetailView.as_view(), name='detail'),
]
