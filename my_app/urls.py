from django.urls import path
from .views import first_page, first_book, second_book, third_book

urlpatterns = [
    path('', first_page),
    path('book/1', first_book),
    path('book/2', second_book),
    path('book/3', third_book),
]