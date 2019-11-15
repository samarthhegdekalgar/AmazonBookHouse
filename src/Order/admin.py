from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'total_price', 'is_cancelled', 'total_price_calculate' )


admin.site.register(Order, OrderAdmin)