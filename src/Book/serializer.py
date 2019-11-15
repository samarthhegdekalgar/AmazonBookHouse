from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'category', 'price', 'short_description', 'image')


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'name', 'author', 'category', 'price', 'short_description', 'image', 'is_deleted')

