from django.shortcuts import render

# Create your views here.

from .models import Project
def project_index(request):
    return render(request, "project/project_index.html", {"project":Project.objects.order_by('-datetime'),} )

def project_details(request, project_id):
    project=get_object_or_404(Project, pk=bug_id)
    return render(request, 'project/project_details.html', {'project':weblog})


