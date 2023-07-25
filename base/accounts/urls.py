from django.urls import path
from .views import get_superusers

urlpatterns = [
    
    path('superusers/', get_superusers, name='superuser-list'),
]