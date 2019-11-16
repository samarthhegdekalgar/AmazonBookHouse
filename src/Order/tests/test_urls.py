from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Order.views import (
    OrderListAPIView,
    OrderCreateAPIView,
    OrderUpdateAPIView,
    OrderDestroyAPIView
)


class TestUrls(SimpleTestCase):
    def test_order_list_urls(self):
        url = reverse('order-list')
        self.assertEquals(resolve(url).func.view_class, OrderListAPIView)

    def test_order_create_urls(self):
        url = reverse('create-order')
        self.assertEquals(resolve(url).func.view_class, OrderCreateAPIView)

    def test_order_update_urls(self):
        url = reverse('update-order', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrderUpdateAPIView)

    def test_order_destroy_urls(self):
        url = reverse('delete-order', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrderDestroyAPIView)