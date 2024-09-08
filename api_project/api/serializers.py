from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year must not be in the future.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class meta:
        model = Author
        fields = ['name', 'books']
