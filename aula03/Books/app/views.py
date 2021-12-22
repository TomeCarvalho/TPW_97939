from django.shortcuts import render

# Create your views here.
from app.models import Author, Book, Publisher


def books_page(request):
    books = Book.objects.all().order_by('title')
    params = {'books': books}
    print(f'{params=}')
    return render(request, 'books.html', params)


def book_details(request, i):
    book = Book.objects.get(id=i)
    params = {'book': book}
    print(f'{params=}')
    return render(request, 'bookdetails.html', params)


def authors_page(request):
    authors = Author.objects.all().order_by('name')
    params = {'authors': authors}
    print(f'{params=}')
    return render(request, 'authors.html', params)


def author_details(request, i):
    author = Author.objects.get(id=i)
    params = {'author': author}
    print(f'{params=}')
    return render(request, 'authordetails.html', params)


def publishers_page(request):
    publishers = Publisher.objects.all().order_by('name')
    params = {'publishers': publishers}
    print(f'{params=}')
    return render(request, 'publishers.html', params)


def publisher_details(request, i):
    publisher = Publisher.objects.get(id=i)
    params = {'publisher': publisher}
    print(f'{params=}')
    return render(request, 'publisherdetails.html', params)

