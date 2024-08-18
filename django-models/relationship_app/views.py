from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Librarian, Library

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}  
    return render(request, 'relationship_app/book_list.html', context)


#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
#Utilize Django’s ListView or DetailView to structure this class-based view.

class SpecificLibrary(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    


