from rest_framework.serializers import ModelSerializer
from app.models import Book


class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "status")
