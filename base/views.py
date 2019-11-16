from django.shortcuts import render, get_object_or_404

# Create your views here.

# Create your views here.
from project.models import Project
from bug.models import Bug
def index(request):
    projects=Project.objects.order_by('-datetime')[0:3]
    bugs=Bug.objects.order_by('-datetime')[0:5]
    return render(request, 'base/index.html', {"projects":projects,"bugs":bugs,})


