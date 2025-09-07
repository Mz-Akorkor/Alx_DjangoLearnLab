from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .models import Library 

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user
            return redirect("list_books")  # redirect to books page (or wherever you prefer)
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})