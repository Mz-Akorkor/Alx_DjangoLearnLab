from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    Secure Book form using Django's ModelForm.
    Handles validation and prevents SQL injection by relying on ORM.
    """
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]