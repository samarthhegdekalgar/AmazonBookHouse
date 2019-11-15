from django.conf import settings
from django.db import models


class Order(models.Model):
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    total_price = models.IntegerField()
    is_cancelled = models.BooleanField()

    def __str__(self):
        return str(self.user)