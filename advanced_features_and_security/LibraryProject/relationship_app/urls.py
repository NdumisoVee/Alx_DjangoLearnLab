from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from django.urls import path
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/', views.register.as_view(), name='register'),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),
    path('books/add_book/', add_book, name='add-book'),
    path('books/edit_book/<int:pk>/', edit_book, name='edit-book'),
    path('books/delete_book/<int:pk>/', delete_book, name='delete-book'),

]


