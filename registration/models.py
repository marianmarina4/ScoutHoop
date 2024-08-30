from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


# Borra foto vieja y sobreescribe la actual
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    
    # Campos Generales
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    ig_link = models.CharField(max_length=100, null=True, blank=True)
    x_link = models.CharField(max_length=100, null=True, blank=True)
    ln_link = models.CharField(max_length=100, null=True, blank=True)
    fbk_link = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
# Se asegura que exista un perfil por cada usuario
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
    
