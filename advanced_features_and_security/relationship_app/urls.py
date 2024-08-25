from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User Registration
    path('register/', views.register, name='register'),
    
    # User Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # User Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Other views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view, add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book_view, name='add_book_view'),
    path('edit_book/', edit_book_view, name='edit_book_view'),
    path('delete_book/', delete_book_view, name='delete_book_view')
]


