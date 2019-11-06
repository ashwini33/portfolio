from django.shortcuts import render

# Create your views here.
def bug_index(request):
    return render(request, "bug/bug_index.html")
