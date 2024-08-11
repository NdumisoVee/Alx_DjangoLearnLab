
# Updating a book
book = Book.objects.filter(title='1984')
book.update(title='Nineteen Eighty-Four')
book.save()