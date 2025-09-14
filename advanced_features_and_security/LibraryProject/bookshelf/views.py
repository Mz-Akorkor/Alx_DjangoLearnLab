from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

"""
Views for managing Book objects.
Access is restricted using Django's built-in @permission_required decorator,
which checks if the logged-in user has the required permission.
"""

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        # logic to save new book
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # logic to update book
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
