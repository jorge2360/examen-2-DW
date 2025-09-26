from django.urls import path
from .views import UsuariosListCreateView

urlpatterns = [
    path('', UsuariosListCreateView.as_view(), name='usuarios'),
]