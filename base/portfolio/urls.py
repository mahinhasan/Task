from django.urls import path
from . import views
from .views import*
urlpatterns = [
    # path('create/',views.project_alt_view),
    # path('<int:pk>/',views.project_alt_view,),
    # path('<int:pk>/update/',views.project_update_view),
    # path('<int:pk>/delete',views.project_delete_view,),
    path('projects/',views.myProjects),
    path('projects/<int:id>/', views.myProjects, name='my_projects'),
    path('projects/saveFile/',views.saveFile),
    # path('projects/getFile/<int:id>/', views.getFile, name='get_file'),
    path('projects/getImage/<str:filename>/', views.getImage, name='get_image'),
    path('contact/',views.contact_me,name='contact'),
]

