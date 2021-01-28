from django import forms
from .models import Climbs

class DateInput (forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

class ClimbsForm(forms.ModelForm):
    class Meta:
        model = Climbs
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': '50px'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any comments/notes here.'})
        }
        labels = {
            'name': 'Route Name',
            'typeOfClimb': 'Boulder or Sport Climb?',
            'state': 'State (use abbreviation)',
        }