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