from django.test import SimpleTestCase
from django.urls import reverse, resolve
from User.views import (
    UserListAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView
)


class TestUrls(SimpleTestCase):
    def test_user_list_urls(self):
        url = reverse('user-list')
        self.assertEquals(resolve(url).func.view_class, UserListAPIView)

    def test_user_create_urls(self):
        url = reverse('create-user')
        self.assertEquals(resolve(url).func.view_class, UserCreateAPIView)

    def test_user_update_urls(self):
        url = reverse('update-user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserUpdateAPIView)

    def test_user_destroy_urls(self):
        url = reverse('delete-user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserDestroyAPIView)