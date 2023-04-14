from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Credentials", {"fields": ("username", "password", "is_active")}),
        ("Personal Info", {"fields": ("email", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, CustomUserAdmin)
