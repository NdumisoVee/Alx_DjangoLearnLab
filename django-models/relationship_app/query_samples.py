from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Using related_name 'books' from the ForeignKey
    return books


# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using related_name 'libraries' from the ManyToManyField
    return books


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(library=library_name)
    librarian = library.librarian  # Using related_name 'librarian' from the OneToOneField
    return librarian
