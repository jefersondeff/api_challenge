from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from .constants import BOOK_AVAILABLE, BOOK_BORROWED


class Book(models.Model):

    BOOK_STATUS_CHOICE = (
        (BOOK_AVAILABLE, BOOK_AVAILABLE),
        (BOOK_BORROWED, BOOK_BORROWED),
    )

    title = models.CharField("Titulo", max_length=100)
    description = models.CharField("Descrição", max_length=300)
    auth = models.CharField("Autor", max_length=100)
    number_page = models.IntegerField("Numero de páginas")
    status = models.CharField(
        "Status", max_length=100, choices=BOOK_STATUS_CHOICE, blank=False
    )
    date_reserved = models.DateTimeField("Data reserva", blank=True, null=True)

    def __str__(self):
        return self.title

    def reserved(self):
        self.status = BOOK_BORROWED
        self.date_reserved = datetime.now() + timedelta(days=3)
        self.save()

    def days_of_delay(self):
        if self.date_reserved:
            return (self.date_reserved - timezone.now()).days
        return 0

    class Meta:
        db_table = "book"


class Client(models.Model):
    name = models.CharField("Nome", max_length=100)
    books = models.ManyToManyField(Book, related_name="books", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "client"

