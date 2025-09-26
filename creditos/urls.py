from django.urls import path
from .views import creditos

urlpatterns = [
    path('', creditos, name='creditos'),
]