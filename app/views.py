from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import Book
from app.serializers import BookListSerializer


class BookList(ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookListSerializer
