from django.shortcuts import render

# Create your views here.

from .models import Project
def index(request):
    projects=Project.objects
    return render(request, 'project/index.html', {"projects":projects})

