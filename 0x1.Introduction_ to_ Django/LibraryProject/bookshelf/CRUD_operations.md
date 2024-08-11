# CRUD Operations for Book Model

## 1. Create a Book Instance

### Command:
```python
from bookshelf.models import Book

# Creating a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#Expected Output
<Book: 1984>

#documentation for read.py
from bookshelf.models import Book

# Retrieving the book we just created
book = Book.objects.get(title="1984")

# Displaying all attributes
book_details = {
    "Title": book.title,
    "Author": book.author,
    "Publication Year": book.publication_year,
}
book_details

#Expected Output:

{'Title': '1984', 'Author': 'George Orwell', 'Publication Year': 1949}

#documentation for update.py

from bookshelf.models import Book

# Retrieving the book instance
book = Book.objects.get(title="1984")

# Updating the title
book.title = "Nineteen Eighty-Four"
book.save()

# Displaying updated book details
updated_book_details = {
    "Title": book.title,
    "Author": book.author,
    "Publication Year": book.publication_year,
}
updated_book_details

#Expected Output:

{'Title': 'Nineteen Eighty-Four', 'Author': 'George Orwell', 'Publication Year': 1949}

#documentation for delete 
from bookshelf.models import Book

# Deleting the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirming the deletion by trying to retrieve all books
remaining_books = Book.objects.all()
list(remaining_books)

#Expected Output:
[]