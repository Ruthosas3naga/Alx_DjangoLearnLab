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
    


