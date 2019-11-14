from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    short_description = models.TextField(max_length=140)
    image = models.ImageField()

    def __str__(self):
        return self.name