from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

# Create your views here.
from project.models import Project
from bug.models import Bug
def index(request):
    projects=Project.objects.order_by('-datetime')[0:3]
    bugs=Bug.objects.order_by('-datetime')[0:5]
    return render(request, 'base/index.html', {"projects":projects,"bugs":bugs,})
def contact(request):
    return render(request,'base/contact.html',)

def dropmessage(request):
    return render(request, 'base/drop_message_form.html')
def confirm(request):
    from .sendmessage import telegram_bot_sendtext
    name=str(request.GET["name"])
    email=str(request.GET["email"])
    message=str(request.GET["message"])
    full_message=(f"Message from {name} ({email})\n"
       f"Message:\n"
       f"{message}")

    test = telegram_bot_sendtext(full_message)
    return HttpResponse(email)


