from django.shortcuts import render, redirect

# Create your views here.
from app.models import *
from app.forms import *


def books_page(request):
    print(f'{request.method=}')
    invalid = True
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            invalid = False
            books = Book.objects.filter(title__icontains=request.POST['book_title'],
                                        authors__name__icontains=request.POST['author_name'],
                                        publisher__name__icontains=request.POST['publisher_name']).distinct()
    if invalid:  # No POST request or invalid POST request
        form = BookSearchForm()
        form.book_title = form.author_name = form.publisher_name = ''
        books = Book.objects.all()
    params = {'form': form, 'invalid': invalid, 'boks': books}
    return render(request, 'books.html', params)


# def books_page(request):
#     book_title = request.POST['book_title'] if 'book_title' in request.POST else ''
#     author_name = request.POST['author_name'] if 'author_name' in request.POST else ''
#     publisher_name = request.POST['publisher_name'] if 'publisher_name' in request.POST else ''
#     books = Book.objects.filter(title__icontains=book_title,
#                                 authors__name__icontains=author_name,
#                                 publisher__name__icontains=publisher_name).distinct()
#     params = {'boks': books}
#     print(f'View: books_page\n{params=}')
#     return render(request, 'books.html', params)


# def booksearch(request):
#     for input_field in ('book_name', 'author_name', 'publisher_name'):
#         if input_field in request.POST:
#             book_name = request.POST['book_name']
#             author_name = request.POST['author_name']
#             publisher_name = request.POST['publisher_name']
#             books = Book.objects.filter(title__icontains=book_name,
#                                         authors__name__icontains=author_name,
#                                         publisher__name__icontains=publisher_name).distinct()
#             return render(request, 'books.html',
#                           {'boks': books, 'book_name': book_name, 'author_name': author_name,
#                            'publisher_name': publisher_name})
#     return render(request, 'booksearch.html', {'error': False})


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


def booksearch(request):
    for input_field in ('book_name', 'author_name', 'publisher_name'):
        if input_field in request.POST:
            book_name = request.POST['book_name']
            author_name = request.POST['author_name']
            publisher_name = request.POST['publisher_name']
            books = Book.objects.filter(title__icontains=book_name,
                                        authors__name__icontains=author_name,
                                        publisher__name__icontains=publisher_name).distinct()
            return render(request, 'books.html',
                          {'boks': books, 'book_name': book_name, 'author_name': author_name,
                           'publisher_name': publisher_name})
    return render(request, 'booksearch.html', {'error': False})


def authorsearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authors.html', {'authors': authors, 'query': query})
        return render(request, 'authorsearch.html', {'error': True})
    return render(request, 'authorsearch.html', {'error': False})


def author_insert(request):
    if 'name' not in request.POST or 'email' not in request.POST:
        return render(request, 'author_insert.html', {'error': True})
    name = request.POST['name']
    email = request.POST['email']
    Author(name=name, email=email).save()
    return redirect(authors_page)


def author_edit(request, i):
    if 'name' not in request.POST or 'email' not in request.POST:
        return render(request, 'author_edit.html', {'error': True, 'author': Author.objects.get(id=i)})
    author = Author.objects.get(id=i)
    name = request.POST['name']
    email = request.POST['email']
    if name and email:
        author.name = name
        author.email = email
        author.save()
        return redirect(authors_page)
    return render(request, 'author_edit.html')
