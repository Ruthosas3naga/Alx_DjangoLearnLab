from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter



class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        book_filter = self.request.query_params.get('book', None)
        if book_filter is not None:
            queryset = queryset.filter(name__icontains=book_filter)
        return queryset

class BookViewSet(viewsets.ModelViewSet):
    
    # Retrieve a single book by ID
    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # Create a new book
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing book by ID
    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update an existing book by ID
    def partial_update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete an existing book by ID
    def destroy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdminBookViewSet(viewsets.MoelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer

    filter_backends = [filter.DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    
    search_fields = ['title', 'author__name']
    
    
    ordering_fields = ['title', 'publication_year']

from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact'],
            'publication_year': ['exact', 'gte', 'lte'],
        }

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
