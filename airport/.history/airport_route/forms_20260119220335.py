from django import forms
from .models import Airport, Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['airport_code_from', 'airport_code_to', 'position', 'duration', 'distance']
        widgets = {
            'duration': forms.TimeInput(format='%H:%M:%S'),
        }
        
class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'name', 'city', 'country']