from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView

router = DefaultRouter()
router.register(r'books', ListView, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', ListView.as_view(), name='book-list'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/detail/<int:pk>/', DetailView.as_view(), name='book-detail'),
    
]

