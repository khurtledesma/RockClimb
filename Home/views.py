from django.shortcuts import render
from .models import Climbs

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
    context = {
        'count': count,
        'climbs': climbs,
        'completedClimb': completedClimb,
        'completedClimbCount': completedClimbCount,
        'notCompletedClimb': notCompletedClimb,
        'notCompletedClimbCount': notCompletedClimbCount,
    }
    return render(request, 'climbs.html', context)

def newClimb(request):
    return render(request, 'newClimb.html')