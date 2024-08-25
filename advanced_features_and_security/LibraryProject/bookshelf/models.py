from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2024)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

  
    def __str__(self):
        return self.username


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a regular user with an email, date of birth, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not date_of_birth:
            raise ValueError('The Date of Birth field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a superuser with an email, date of birth, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, date_of_birth, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Specify that the CustomUserManager should be used for managing CustomUser instances
    objects = CustomUserManager()

    def __str__(self):
        return self.email
