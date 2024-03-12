from django.urls import path
from .views import *


urlpatterns = [
    path('books/', get_books),
    path('books/', get_books_by_id),
    path('books-delete/', delete_books),
    path('books-post/', post_books),
    path('books-put/', put_books)
]