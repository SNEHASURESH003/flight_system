from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Route(models.Model):
    airport_code_from = models.ForeignKey(Airport, related_name='routes_from', on_delete=models.CASCADE)
    airport_code_to = models.ForeignKey(Airport, related_name='routes_to', on_delete=models.CASCADE)
    position 