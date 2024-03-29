from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


