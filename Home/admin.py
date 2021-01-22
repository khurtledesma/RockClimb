from django.contrib import admin
from .models import Climbs

# Register your models here.

class ClimbsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'typeOfClimb')
    
admin.site.register(Climbs, ClimbsAdmin)