from django.test import TestCase, Client
from django.urls import reverse
from User.models import User



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('user-list')
        self.create_user = reverse('create-user')
        self.delete_user = reverse('delete-user', args=[3])
        self.update_user = reverse('update-user', args=[4])

    def test_user_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_user_create_POST(self):
        response = self.client.post(self.create_user, {
            'name': 'testuser',
            'email': 'testuser@company.com',
            'password': 'password'
        })
        self.assertEquals(response.status_code, 201)
        ack = User.objects.all()[0]
        self.assertEquals(ack.name, 'testuser')

    def test_user_create_POST_no_data(self):
        response = self.client.post(self.create_user)
        self.assertEquals(response.status_code, 400)
        self.assertNotEquals(response.status_code, 201)

    def test_user_delete(self):
        User.objects.create(name='testuser', email='testuser@gmail.com', password='pass')
        name = User.objects.all()[0]
        response = self.client.delete(self.delete_user)
        self.assertEquals(response.status_code, 204)

    def test_user_update(self):
        User.objects.create(name='testuser', email='testuser@gmail.com', password='pass')
        name = User.objects.all()[0]
        self.assertEquals(name.name, 'testuser')
        response = self.client.put(self.update_user, '{"name":"updated", "email":"email@company.com","password":"pass"}',
                                   'application/json')
        self.assertEquals(response.status_code, 200)
        name = User.objects.all()[0]
        self.assertEquals(name.name, 'updated')
