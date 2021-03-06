"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings    #custom_configuration
from django.conf.urls.static import static  #custom_configuration

import project.views
import base.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base.views.index, name="homepage"),
    path('contact/', base.views.dropmessage, name="contact"),
    path('dropmessage/', base.views.dropmessage, name="dropmessage"),
    path('confirm/', base.views.confirm, name="confirm"),
    path('bug/', include('bug.urls')),
    path('weblog/', include('weblog.urls')),
    path('project/', include('project.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
