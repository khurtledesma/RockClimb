import requests
from django.shortcuts import render
from .models import Climbs

# Create your views here.

def index(request):
    weatherUrl = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=319ce877549b8a92d0ca175e58407932'
    city = 'Austin'

    r = requests.get(weatherUrl.format(city)).json()

    weather = {
        'city': city,
        'temp': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'], 
    }
    
    context = {
        'weather': weather
        }

    return render(request, 'index.html', context)

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
    return render(request, 'newClimb.html')