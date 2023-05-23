from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(auth_admin.UserAdmin):
    model = CustomUser
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields':('user_vsc', 'password_vsc','biography',)}),
    )