from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    model = User
    ordering = ['username', 'email', 'phone']
    list_display = []
    list_filter = ['username', 'email']

    @staticmethod
    def get_output_full_name(obj):
        return obj.get_full_name()

    @staticmethod
    def get_output_phone(obj):
        return obj.get_phone()

    get_output_full_name.short_description = 'ФИ(Ник)'
    get_output_phone.short_description = 'Номер телефона'


