from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager



class Post(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add tags for each post
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    