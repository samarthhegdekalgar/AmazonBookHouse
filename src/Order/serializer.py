from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')
    book_name = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = Order
        fields = ('user_name', 'book_name', 'total_price', 'is_cancelled')


class OrderUpdateSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    book_name = serializers.CharField(source='book.name')

    class Meta:
        model = Order
        fields = ('pk', 'user_name', 'book_name', 'total_price', 'is_cancelled')

