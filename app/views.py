from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.constants import BOOK_BORROWED
from app.models import Book, Client
from app.serializers import BookListSerializer
from app.src.calculate_fine import calculate_fine


class BookList(ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookReserve(APIView):
    def post(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response("Book does not exist.", status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client.objects.get(id=request.data.get("client_id"))
        except ObjectDoesNotExist:
            return Response(
                "Client does not exist.", status=status.HTTP_400_BAD_REQUEST
            )

        client.books.add(book)
        book.reserved()
        content = {
            "book": book.title,
            "status": book.status,
            "date_reserved": book.date_reserved,
        }
        return Response(content)


class ClientBook(APIView):
    def post(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
        except ObjectDoesNotExist:
            return Response(
                "Client does not exist.", status=status.HTTP_400_BAD_REQUEST
            )

        content = {
            "client": client.name,
            "books": [
                {"title": book.title, "multa": calculate_fine(book.days_of_delay())}
                for book in client.books.all()
            ],
        }
        return Response(content)
