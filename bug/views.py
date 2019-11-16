from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Bug
def bug_index(request):
    return render(request, "bug/bug_index.html", {"bugs":Bug.objects.order_by('-datetime'),} )

def bug_details(request, bug_id):
    bug=get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/bug_details.html', {'bug':bug})

