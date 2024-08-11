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