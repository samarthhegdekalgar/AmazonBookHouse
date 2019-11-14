from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'price', 'short_description', 'image')


admin.site.register(Book, BookAdmin)