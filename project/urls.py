from django.urls import path
from . import views
urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:project_id>',views.project_details, name='project_details'),
    
]

