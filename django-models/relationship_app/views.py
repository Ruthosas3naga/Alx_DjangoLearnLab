from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Librarian, Library

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}  
    return render(request, 'relationship_app/list_books.html', context)

from .models import Library
from django.views.generic.detail import DetailView


class SpecificLibrary(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    
# relationship_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'


# Logout View can also be used directly from auth.views
class CustomLogoutView(LogoutView):
    template_name = 'auth/logout.html'


# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to some page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# In relationship_app/views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_check(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def librarian_check(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def member_check(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from . models import Book
from .forms import BookForm

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        # Handle book creation logic here
        # For example, using a form to create a new book
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book update logic here
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Redirect to the book's detail page
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book deletion logic here
        book.delete()
        return redirect('book_list')  # Redirect to the list of books
    return render(request, 'relationship_app/delete_book.html', {'book': book})



    


