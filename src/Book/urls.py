from django.urls import path
from .views import BookListAPIView, BookCreateAPIView, BookUpdateAPIView, BookDestroyAPIView, BookSearchAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('create/', BookCreateAPIView.as_view(), name='create-book'),
    path('update/<int:pk>', BookUpdateAPIView.as_view(), name='update-book'),
    path('delete/<int:pk>', BookDestroyAPIView.as_view(), name='delete-book'),
    path('search/', BookSearchAPIView.as_view(), name='search-book')
]