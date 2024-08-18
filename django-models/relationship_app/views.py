from django.shortcuts import render

from .models import Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})



# Admin View
def is_admin(user):
    return user.userprofile.role == 'Admin'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})


# Member View
def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})


# Librarian View
def is_librarian(user):
    return user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})

