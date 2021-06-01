from django.urls import path
from .views import handle_author, handle_authors, handle_book, handle_books

urlpatterns = [
    path('authors/', handle_authors),
    path('authors/<int:author_id>/', handle_author),
    path('books/', handle_books),
    path('books/<int:book_id>/', handle_book)
]
