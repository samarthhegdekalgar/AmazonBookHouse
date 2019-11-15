from django.urls import path
from .views import OrderListAPIView, OrderCreateAPIView, OrderUpdateAPIView, OrderDestroyAPIView

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('create/', OrderCreateAPIView.as_view(), name='create-order'),
    path('update/<int:pk>', OrderUpdateAPIView.as_view(), name='update-order'),
    path('delete/<int:pk>', OrderDestroyAPIView.as_view(), name='delete-order'),
]