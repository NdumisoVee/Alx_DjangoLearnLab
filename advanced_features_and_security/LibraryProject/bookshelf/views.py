# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm


@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'edit_book.html', {'book': book})


@permission_required('your_app_name.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'create_book.html')


@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})


def search_books(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'book_list.html', {'books': books, 'form': form})
    return render(request, 'book_list.html', {'form': form})