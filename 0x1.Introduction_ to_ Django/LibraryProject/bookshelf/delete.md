
# Deleting a book
book_to_delete = Book.objects.get(title='Nineteen Eighty-Four').delete() 
books_after_deletion = Book.objects.all()
