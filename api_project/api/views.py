from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        book_filter = self.request.query_params.get('book', None)
        if book_filter is not None:
            queryset = queryset.filter(name__icontains=book_filter)
        return queryset
