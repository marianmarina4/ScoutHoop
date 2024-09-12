from django.db import models
from registration.models import Profile


def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Player.objects.get(pk=instance.pk)
        old_instance.avatar.delete()
    return 'players/' + filename

class Player(models.Model):
    agent = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='players')
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    first_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    height = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    position = models.CharField(max_length=20, choices=[('base', 'Base'), ('escolta', 'Escolta'), ('alero', 'Alero'), ('alapivot', 'Ala-Pivot'), ('pivot', 'Pivot')])
    status = models.CharField(max_length=20, choices=[('available', 'Disponible'), ('not available', 'No Disponible')])
    yt_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def youtube_embed(self):
        if self.yt_link:
            return self.yt_link.replace("watch?v=", "embed/")
        return None


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_played = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.team_name} ({self.country}) - {self.year_played}'