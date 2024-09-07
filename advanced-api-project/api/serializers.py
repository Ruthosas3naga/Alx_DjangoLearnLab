from models import Book, Author
from rest_framework import serializers
import datetime
from rest_framework.serializers import ModelSerializer 

class BookSerializers(serializers.ModelSerializer):
    class meta:
       model = Book
       fields = '__all__'

#This is to validate the publication year not to be in the future 
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

#This is to create a nested serializer by calling the BookSeria;ization. This simply means we what to make use of the fields in the BookSerializer
class AuthorSerializers(serializers.ModelSerializer):
    books = BookSerializers(many=True, read_only=True)

    class meta:
        model = Author
        fields = ['name', 'boooks']
