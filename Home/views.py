from django.shortcuts import render
from .models import Climbs

# Create your views here.

def index(request):
    return render(request, 'index.html')

def climbs(request):
    climbs = Climbs.objects.all()
    count = climbs.count()
    context = {
        'count': count,
        'climbs': climbs,
    }
    return render(request, 'climbs.html', context)

def newClimb(request):
    return render(request, 'newClimb.html')