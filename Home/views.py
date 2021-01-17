from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def climbs(request):
    return render(request, 'climbs.html')

def newClimb(request):
    return render(request, 'newClimb.html')