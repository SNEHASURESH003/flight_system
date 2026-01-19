from django import forms
from .models import Route, Airport

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['airport_code_from', 'airport_code_to', 'position', 'duration']