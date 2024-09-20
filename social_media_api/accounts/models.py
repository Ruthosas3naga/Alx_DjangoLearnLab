from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/pics', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username