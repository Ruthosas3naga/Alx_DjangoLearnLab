from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse ("Welcome to Django Alx django lab")

# Create your views here
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post

@permission_required('app_name.can_create_post', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # Handle post creation logic
        ...
    return render(request, 'create_post.html')

@permission_required('app_name.can_edit_post', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle post edit logic
        ...
    return render(request, 'edit_post.html', {'post': post})

@permission_required('app_name.can_delete_post', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all book records from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})


# LibraryProject/bookshelf/views.py

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle the form data
            print(form.cleaned_data)
            return redirect('some_success_page')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})

