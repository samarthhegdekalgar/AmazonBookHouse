from django.conf import settings
from django.db import models


class Order(models.Model):
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0, null=True)
    is_cancelled = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.user)

    def total_price_calculate(self):
        self.total_price += self.book.price
        return self.total_price


'''
The Order class contains details of book selected by the consumer and added to the cart
    :__str__ function returns the string value of user
    : total_price_calculate returns the total price of the book added in the cart
'''