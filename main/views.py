from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def books(request):
    return render(request, 'book.html')

def create_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'])
    return redirect('/books')

def create_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'])
    return redirect('/authors')

def authors(request):
    return render(request, 'author.html')