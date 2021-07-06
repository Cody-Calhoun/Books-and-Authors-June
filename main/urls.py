from django.urls import path, include
from .views import *
urlpatterns = [
    path('books', books),
    path('books/create', create_book),
    path('authors', authors),
    path('authors/create', create_author),
]
