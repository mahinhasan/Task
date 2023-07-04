

from django.urls import path,include
# from .views import home
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:pk>/',views.ancient_details,name='details'),
    # path('ancient_create/',views.ancient_create,name='create'),
] 