from django.test import TestCase
from Order.models import Order
from User.models import User
from Book.models import Book


class TestModels(TestCase):
    def setUp(self):
        self.user_obj = User.objects.create(name='testUser',
                                            email='testUser@company.com',
                                            password='pass')

        self.book_obj = Book.objects.create(name='testbook',
                                            author='testauthor',
                                            category='testcategory',
                                            price=100,
                                            short_description='testbook short description')
        self.order_obj = Order.objects.create(user=self.user_obj,
                                              book=self.book_obj)

    def test_order_object_create(self):
        ack = self.order_obj
        print(ack)
        self.assertEquals(ack.user.name, self.user_obj.user.name)
        self.assertEquals(ack.book.name, self.book_obj.book.name)


