from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer, OrderUpdateSerializer
from .models import Order
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all().filter(is_cancelled=False)
    serializer_class = OrderSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    lookup_field = 'pk'


class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_cancelled = True
        instance.save()


'''
The Api view created for OrderApp
Crud Operations has been performed 

class OrderListAPIView is for get data 

class OrderCreateAPIView(CreateAPIView): In this method 'create function' has been created for 
                                        creating the data

class OrderDestroyAPIView(DestroyAPIView): In this a destroy method has been created to delete the order details


'''