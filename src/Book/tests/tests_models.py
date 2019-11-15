from django.test import TestCase
from Book.models import Book


class TestModels(TestCase):
    def setUp(self):
        self.book_obj = Book.objects.create(name='testbook',
                                            author='testauthor',
                                            category='testcategory',
                                            price=100,
                                            short_description='testbook short description')

    def test_book_object_create(self):
        ack = self.book_obj
        self.assertEquals(ack.name, 'testbook')
        self.assertEquals(ack.author, 'testauthor')
        self.assertEquals(ack.category, 'testcategory')
        self.assertEquals(ack.price, 100)
        self.assertEquals(ack.short_description, 'testbook short description')
        self.assertNotEquals(ack.name, 'user')
        self.assertNotEquals(ack.author, 'author')
        self.assertNotEquals(ack.category, 'password')
        self.assertNotEquals(ack.price, 344)
        self.assertNotEquals(ack.short_description, 'Its not a valid data')


