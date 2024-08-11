
# Updating a book
book = Book.objects.title(title='1984')
book.update(title='Nineteen Eighty-Four')
book.save()