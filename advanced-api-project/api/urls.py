from django.urls import path
from views import CreateView, ListView, DetailView, DeleteView, UpdateView

urlpatterns = [
    path('/books/create', CreateView.as_view(), name='book-create'),
    path('/books/', ListView.as_view(), name='book-list'),
    path('/books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/update', UpdateView.as_view(), name='book-update'),
    path('books/delete', DeleteView.as_view(), name='book-delete'),
]