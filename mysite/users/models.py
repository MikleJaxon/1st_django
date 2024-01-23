from django.db import models
from django.contrib.auth.models import User


class Profie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='profiel_images')
    contact_number = models.CharField(max_length=20, default="+7123456789")
    
    def __str__(self):
        return self.user.username