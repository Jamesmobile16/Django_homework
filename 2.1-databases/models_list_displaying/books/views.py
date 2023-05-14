from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)

def book_by_date_view(request, detail_date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=detail_date)
    next_page = Book.objects.filter(pub_date__gt=detail_date).order_by('pub_date').first()
    previous_page = Book.objects.filter(pub_date__lt=detail_date).order_by('-pub_date').first()
    context = {
        'books': books,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)

