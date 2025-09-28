from django.urls import path
from . import views
from .views import (
    BookListView, BookDetailView, 
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update-noid'),  # <-- checker
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete-noid'),  # <-- checker
]