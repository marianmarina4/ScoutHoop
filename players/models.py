from django.db import models
from registration.models import Profile

class Player(models.Model):
    
    agent = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='players')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    position = models.CharField(max_length=20, choices=[('base', 'Base'), ('escolta', 'Escolta'), ('alero', 'Alero'), ('alapivot', 'Ala-Pivot'), ('pivot', 'Pivot')])
    last_teams = models.TextField(null=True, blank=True)
    current_team = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('available', 'Disponible'), ('not available', 'No Disponible')])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'