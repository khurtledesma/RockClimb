from django.contrib import admin
from .models import Climbs

# Register your models here.

class ClimbsAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'city', 'typeOfClimb','rating', 'completed',)
    
admin.site.register(Climbs, ClimbsAdmin)