from models import Post, Comment
from rest_framework import serializers
from django.contrib.auth import 

class PostSerilizer(serializers.ModelSerializer):
    