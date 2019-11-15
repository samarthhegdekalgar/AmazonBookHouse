from django.test import TestCase
from User.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user_obj = User.objects.create(name='testUser',
                                            email='testUser@company.com',
                                            password='pass')

    def test_user_object_create(self):
        ack = self.user_obj
        self.assertEquals(ack.name, 'testUser')
        self.assertEquals(ack.email, 'testUser@company.com')
        self.assertEquals(ack.password, 'pass')
        self.assertNotEquals(ack.name, 'user')
        self.assertNotEquals(ack.name, 'user@company.com')
        self.assertNotEquals(ack.name, 'password')


