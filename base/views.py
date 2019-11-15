from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from project.models import Project
def index(request):
    projects=Project.objects
    return render(request, 'base/index.html', {"projects":projects})


