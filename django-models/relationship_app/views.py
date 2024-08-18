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
    return render(request, 'auth/register.html', {'form': form})

    


