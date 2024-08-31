from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'
