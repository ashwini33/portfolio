from django.urls import path
from . import views
urlpatterns = [
    path('', views.weblog_index, name='weblog_index'),
    path('<int:weblog_id>',views.weblog_details, name='weblog_details'),
    
]

