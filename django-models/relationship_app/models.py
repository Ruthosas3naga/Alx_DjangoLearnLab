from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self, name):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Define role choices
    role_choices = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    # Link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=role_choices, default='Member')
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'
