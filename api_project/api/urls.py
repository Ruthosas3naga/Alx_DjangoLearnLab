from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListAPIView

router = DefaultRouter()
router.register(r'my-books', BookListAPIView)

urlpatterns = [
    path("api/books", BookListAPIView.as_view(), name="book_list_create"),
]

