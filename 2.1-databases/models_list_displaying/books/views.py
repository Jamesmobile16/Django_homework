from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    books = [book for book in books_objects]
    # pub_date = str(Book.pub_date)
    next_page = Book.objects.filter(pub_date__lt=date).values('pub_date')
    previous_page = Book.objects.filter(pub_date__gt=date).values('pub_date')

    context = {
        'books': books,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)

