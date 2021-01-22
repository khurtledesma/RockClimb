from django import forms
from .models import Climbs

class ClimbsForm(forms.ModelForm):
    class Meta:
        model = Climbs
        fields = [
            'name',
            'state',
            'city',
            'typeOfClimb',
            'completed',
            'rating',
        ]