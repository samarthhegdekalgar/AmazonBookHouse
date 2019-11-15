from django.test import TestCase, Client
from django.urls import reverse
from Book.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('book-list')
        self.create_book = reverse('create-book')
        self.delete_book = reverse('delete-book', args=[2])
        self.update_book = reverse('update-book', args=[3])

    def test_book_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_book_create_POST(self):
        response = self.client.post(self.create_book, {
            'name': 'testbook',
            'author': 'testauthor',
            'category': 'testcategory',
            'price': 100,
            'short_description': 'test case short description in book app',

        })
        self.assertEquals(response.status_code, 201)
        ack = Book.objects.all()[0]
        self.assertEquals(ack.name, 'testbook')

    def test_book_create_POST_no_data(self):
        response = self.client.post(self.create_book)
        self.assertEquals(response.status_code, 400)
        self.assertNotEquals(response.status_code, 201)

    def test_book_delete(self):
        Book.objects.create(name='testbook', author='testauthor', category='testcategory', price=100)
        name = Book.objects.all()[0]
        response = self.client.delete(self.delete_book)
        self.assertEquals(response.status_code, 204)

    def test_book_update(self):
        Book.objects.create(name='testbook', author='testauthor', category='testcategory', price=100)
        name = Book.objects.all()[0]
        self.assertEquals(name.name, 'testbook')
        response = self.client.put(self.update_book, '{"name":"updated", '
                                                     '"author":"testauthor",'
                                                     '"category":"testcategory",'
                                                     '"price":100,'
                                                     '"short_description": "test case short description in book app"}',
                                   'application/json')
        self.assertEquals(response.status_code, 200)
        name = Book.objects.all()[0]
        self.assertEquals(name.name, 'updated')
