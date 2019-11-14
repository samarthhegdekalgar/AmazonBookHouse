from django.urls import path
from .views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='create-user'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update-user'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='delete-user'),
]