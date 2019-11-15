from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')


<<<<<<< HEAD
admin.site.register(User)
=======
admin.site.register(User, UserAdmin)
>>>>>>> 56d60130bcee338e735c9228e85505793ce03006
