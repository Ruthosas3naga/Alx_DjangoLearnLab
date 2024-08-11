# CRUD Operations for Book Model

## 1. Create a Book Instance

### Command:
```python
from bookshelf.models import Book

# Creating a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#Expected Output
<Book: 1984>
