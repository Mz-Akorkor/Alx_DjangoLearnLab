from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns shown in list view

    search_fields = ("title", "author")  # search box

    list_filter = ("publication_year",)  # sidebar filter
