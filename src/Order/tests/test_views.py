from django.test import TestCase, Client
from django.urls import reverse
from Order.models import Order
from User.models import User
from Book.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('order-list')
        self.create_order = reverse('create-order')
        self.delete_order = reverse('delete-order', args=[5])
        self.update_order = reverse('update-order', args=[6])

    def test_order_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_order_create_POST(self):
        self.user_obj = User.objects.create(name='testUser',
                                            email='testUser@company.com',
                                            password='pass')

        self.book_obj = Book.objects.create(name='testbook',
                                            author='testauthor',
                                            category='testcategory',
                                            price=100,
                                            short_description='testbook short description')

        response = self.client.post(self.create_order, {
            'user': self.user_obj,
            'book': self.book_obj,
        })
        self.assertEquals(response.status_code, 201)
        ack = Order.objects.all()[0]
        self.assertEquals(ack.user.name, self.user_obj.name)
        self.assertEquals(ack.book.name, self.book_obj.name)

    def test_order_create_POST_no_data(self):
        response = self.client.post(self.create_order)
        self.assertEquals(response.status_code, 400)
        self.assertNotEquals(response.status_code, 201)

    def test_order_delete(self):
        self.user_obj = User.objects.create(name='testUser',
                                            email='testUser@company.com',
                                            password='pass')

        self.book_obj = Book.objects.create(name='testbook',
                                            author='testauthor',
                                            category='testcategory',
                                            price=100,
                                            short_description='testbook short description')

        Order.objects.create(user=self.user_obj.name, book=self.book_obj.name)
        name = Order.objects.all()[0]
        response = self.client.delete(self.delete_order)
        self.assertEquals(response.status_code, 204)

    def test_order_update(self):
        self.user_obj = User.objects.create(name='testUser',
                                            email='testUser@company.com',
                                            password='pass')

        self.book_obj = Book.objects.create(name='testbook',
                                            author='testauthor',
                                            category='testcategory',
                                            price=100,
                                            short_description='testbook short description')

        Order.objects.create(user=self.user_obj.name, book=self.book_obj.name )
        name = Order.objects.all()[0]
        self.assertEquals(name.name, 'testuser')
        response = self.client.put(self.update_order, '{"name":"updated", "email":"email@company.com","password":"pass"}',
                                   'application/json')
        self.assertEquals(response.status_code, 200)
        name = Order.objects.all()[0]
        self.assertEquals(name.name, 'updated')
