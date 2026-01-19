from django.db import models
from django.forms import ValidationError

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Route(models.Model):
    POSITION_CHOICES = [('left', 'Left'), ('right', 'Right')]
    airport_code_from = models.ForeignKey(Airport, related_name='routes_from', on_delete=models.CASCADE)
    airport_code_to = models.ForeignKey(Airport, related_name='routes_to', on_delete=models.CASCADE)
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    duration = models.DurationField()
    distance = models.FloatField(de)
    def __str__(self):
        return f"Route from {self.airport_code_from.code} to {self.airport_code_to.code} - {self.position},{self.duration}"
    

    def clean(self):
      if self.airport_code_from == self.airport_code_to:
            raise ValidationError("From and To airports must be different.")