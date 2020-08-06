from django.urls import path

from app.views import BookList, BookReserve, ClientBook

urlpatterns = [
    path("books/", BookList.as_view()),
    path("books/<int:id>/reserve", BookReserve.as_view()),
    path("client/<int:client_id>/books", ClientBook.as_view()),
]
