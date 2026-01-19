class AirportRouteForm(forms.Form):
    origin = forms.CharField(label='Origin Airport', max_length=100)
    destination = forms.CharField(label='Destination Airport', max_length=100)