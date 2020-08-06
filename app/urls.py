from django.urls import path
from app.views import BookList


urlpatterns = [
    path("books/", BookList.as_view()),
    # path("", include("app.urls")),
]
