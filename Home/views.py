import requests
from django.shortcuts import render
from .models import Climbs
from .forms import ClimbsForm

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

    context = {
        'form': form
    }
    return render(request, 'newClimb.html', context)

def routeFinder(request):
    city = ('Austin')
    mapUrl = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyCikhDfCw0_pf9qJHUW4GNwIi2x-Iau2P0&q=Austin'
    weatherUrl = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=319ce877549b8a92d0ca175e58407932'
    

    wr = requests.get(weatherUrl.format(city)).json()
    mr = requests.get(mapUrl.format(city))
    

    weather = {
        'city': city,
        'temp': wr['main']['temp'],
        'description': wr['weather'][0]['description'],
        'icon': wr['weather'][0]['icon'], 
    }
    
    context = {
        'weather': weather,
        'map': mr,
        }

    return render(request, 'routeFinder.html',)
