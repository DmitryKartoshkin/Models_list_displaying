from datetime import date

from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_view_1(request):
    template = 'books/book.html'
    books = Book.objects.all()
    for p in books:
        d = str(p.pub_date)
    context = {'books': books,}
    return render(request, template, context)


def books_view_2(request):
    template = 'books/book_data.html'
    pub_date_next = ''
    pub_date_previous = ''
    books_1 = Book.objects.all()
    LIST_ = [str(book.pub_date) for book in books_1]
    LIST_ = list(set(LIST_))
    paginator = Paginator(LIST_, 1)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    d = date.fromisoformat(LIST_[page_number - 1])
    if page.has_next():
        pub_date_next = LIST_[page.number]
    if page.has_previous():
        pub_date_previous = LIST_[page.number - 2]
    books = Book.objects.filter(pub_date=d)
    context = {'books': books, 'page': page, 'next_page': pub_date_next, 'previous_page': pub_date_previous}
    return render(request, template, context)