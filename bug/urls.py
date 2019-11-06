from django.urls import path
from . import views
urlpatterns = [
    path('', views.bug_index, name='bug_index'),
    
]

