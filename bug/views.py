from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Bug
def bug_index(request):
    return render(request, "bug/bug_index.html", {"bugs":Bug.objects.order_by('-datetime'),} )

def bug_details(request, bug_id):
    bug=get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/bug_details.html', {'bug':bug})

from django.db.models import Q

def bug_search(request):
    search_string = request.GET.get('search_string')
    object_list = Bug.objects.filter(
            Q(issue__icontains=search_string) | Q(summary__icontains=search_string)
            )
    #object_list= Bug.objects.filter(issue__icontains='n')
    return render(request, 'bug/bug_search.html', {"bugs":Bug.objects.order_by('-datetime'), "search_string":search_string, "object_list":object_list})
