from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display= ["username", "email", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
