from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from myapp.my_forms import BookForm


# Create your views here.

def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm(request.POST)
    return render(request, 'add_book.html', {'form': form})

    # Book.objects.create(title='River and the Source',
    #                     year=2021,
    #                     category='Fiction',
    #                     cost=600,
    #                     isbn= '34567890',
    #                     published=True)
    # Book.objects.create(title='Kidagaa KImemuozea',
    #                     year=2018,
    #                     category='Politics',
    #                     cost=780,
    #                     isbn= '34678998',
    #                     published=True)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('show_books')


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})
    return None