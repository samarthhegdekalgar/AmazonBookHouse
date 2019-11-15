from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Book.views import (
    BookListAPIView,
    BookCreateAPIView,
    BookUpdateAPIView,
    BookDestroyAPIView
)


class TestUrls(SimpleTestCase):
    def test_book_list_urls(self):
        url = reverse('book-list')
        self.assertEquals(resolve(url).func.view_class, BookListAPIView)

    def test_book_create_urls(self):
        url = reverse('create-book')
        self.assertEquals(resolve(url).func.view_class, BookCreateAPIView)

    def test_book_update_urls(self):
        url = reverse('update-book', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookUpdateAPIView)

    def test_book_destroy_urls(self):
        url = reverse('delete-book', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookDestroyAPIView)