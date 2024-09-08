from django.shortcuts import render
from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework


# Create your views here.
"""
Implementing a List API view for retrieving all books from the Book Model.
This view allows unauthenticated users to have read only access.
"""
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    # allowing filtering by 'author', 'title' or 'publication_year'
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # enabling search functionality by 'title', or 'author' 
    search_fields = ['title', 'author__name']

    # implementing ordering by 'title', or 'publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # default ordering

 # Enabling Pagination to set number of books displayed per page.
    pagination_class = PageNumberPagination


"""
Implementing a Detail API view for retrieving a single book by ID from the Book Model.
This view allows unauthenticated users have read only access.
"""
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#An Author creation view to enable only authenticated and admin users to create new authors."""
class CreateAuthorView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


"""
#Implementing a Create API view for adding new books into the Book Model.Only authenticated users can create books."""
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    permission_classes = [IsAuthenticated]

    # Custom method to handle form submission when creating books
    # def perform_create(self, serializer):
    #     # this sets the created_by field to the current user
    #     serializer.save(created_by=self.request.user) 

"""
An API view for modifying an existing book in the Book Model.
Only authenticated users can update books.
"""
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]

    # # Custom method to handle form submission when updating books
    # def perform_update(self, serializer):
    #    # this sets the updated_by field to the current user
    #    serializer.save(updated_by=self.request.user) 


"""
A Delete view for deleting books instances from the Book Model.
Only authenticated users can delete books.
"""
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
