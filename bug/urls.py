from django.urls import path
from . import views
urlpatterns = [
    path('', views.bug_index, name='bug_index'),
    path('<int:bug_id>',views.bug_details, name='bug_details'),
    
]

