from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.project_alt_view),
    path('<int:pk>/',views.project_alt_view,),
    path('<int:pk>/update/',views.project_update_view),
    path('<int:pk>/delete',views.project_delete_view,),

]
