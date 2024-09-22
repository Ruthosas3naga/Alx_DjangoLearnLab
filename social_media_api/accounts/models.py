from django.contrib.auth.models import AbstractUser, User
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/pics', blank=True, null=True)
    
    # 'followers' field tracks who is following this user, 'following' tracks who the user is following
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_set', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_set', blank=True)

    def __str__(self):
        return self.username

  

