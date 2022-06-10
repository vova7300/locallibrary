from django.shortcuts import render
from .models import Book, Author, BookInstance,  Genre
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    wild_books = Book.objects.filter(title__contains='Сказка')
    number_wild_books = wild_books.count()
    books_containing_genre = Book.objects.filter(genre__name__contains='зки')
    containing_genre = books_containing_genre.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'number_wild_books': number_wild_books, 'books_containing_genre': books_containing_genre,
                 'containing_genre': containing_genre},
    )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


# Create your views here.
