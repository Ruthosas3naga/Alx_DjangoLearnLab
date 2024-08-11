from bookshelf.models import Book

# Deleting the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirming the deletion by trying to retrieve all books
remaining_books = Book.objects.all()
list(remaining_books)

#Expected Output:
[]