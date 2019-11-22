from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Weblog
def weblog_index(request):
    return render(request, "weblog/weblog_index.html", {"weblog":Weblog.objects.order_by('-datetime'),} )

def weblog_details(request, bug_id):
    weblog=get_object_or_404(Weblog, pk=weblog_id)
    return render(request, 'weblog/weblog_details.html', {'weblog':weblog})

