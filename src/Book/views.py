from rest_framework import status, filters
from rest_framework.response import Response
from .serializer import BookListSerializer, BookUpdateSerializer
from .models import Book
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all().filter(is_deleted=False)
    serializer_class = BookListSerializer


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'pk'


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class BookSearchAPIView(ListCreateAPIView):
    search_fields = ['name', 'author', 'category', 'short_description']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer


