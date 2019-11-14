from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name


