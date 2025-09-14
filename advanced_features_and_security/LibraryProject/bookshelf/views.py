from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

"""
Views for managing Book objects.
Access is restricted using Django's built-in @permission_required decorator,
which checks if the logged-in user has the required permission.
"""

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    """
    Create a new Book using Django's ModelForm for validation and safety.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # ✅ ensures validation
            form.save()      # ✅ safe ORM save
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "bookshelf/book_form.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    """
    Edit an existing Book using Django's ModelForm for validation and safety.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():  # ✅ ensures safe updates
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "bookshelf/book_form.html", {"form": form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Security Notes:
# - DEBUG = False disables debug info in production
# - CSRF_COOKIE_SECURE & SESSION_COOKIE_SECURE enforce HTTPS cookies
# - CSP_* headers restrict sources to prevent XSS
# - Queries use Django ORM to avoid SQL injection
