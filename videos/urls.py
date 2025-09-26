from django.urls import path
from .views import VideosListCreateView

urlpatterns = [
    path('', VideosListCreateView.as_view(), name='videos'),
]