import requests
from django.shortcuts import render
from .models import Climbs
from .forms import ClimbsForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

    return render(request, 'index.html')

def climbs(request):

    climbs = Climbs.objects.all()
    count = climbs.count()
    notCompletedClimb = Climbs.objects.filter(completed=False)
    notCompletedClimbCount = notCompletedClimb.count()
    completedClimb = Climbs.objects.filter(completed=True)
    completedClimbCount = completedClimb.count()
    
    climbsData = {
        'count': count,
        'climbs': climbs,
        'completedClimb': completedClimb,
        'completedClimbCount': completedClimbCount,
        'notCompletedClimb': notCompletedClimb,
        'notCompletedClimbCount': notCompletedClimbCount,
    }
    context = {
        'climbsData': climbsData
    }

    return render(request, 'climbs.html', context)

def newClimb(request):
    form = ClimbsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClimbsForm
        return HttpResponseRedirect('/thanks/')

    context = {
        'form': form
    }

    return render(request, 'newClimb.html', context)

def routeFinder(request):
    return render(request, 'routeFinder.html')

def thanks(request):
    return render(request, 'thanks.html')