from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    model = User
    ordering = ['username', 'email', 'phone']
    list_display = ['get_output_full_name', 'get_output_phone']
    list_filter = ['username', 'email']

    def get_output_full_name(self, obj):
        return obj.get_full_name()

    def get_output_phone(self, obj):
        if not obj.phone:
            return 'Нет номера'
        return obj.get_phone()

    get_output_full_name.short_description = 'ФИ(Ник)'
    get_output_phone.short_description = 'Номер телефона'

    fieldsets = (
        ("Авторизация", {'fields': ('username', 'email', 'password')}),
        ("Персональная информация", {
            'fields': (
                'first_name', 'last_name', 'phone',
            )}),
        ("Разрешения", {
            'fields': ('is_staff', 'is_active', 'is_superuser',)}),
        ("Дополнительная информация", {
            'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             'fields': (
                 'username',
                 'email',
                 'phone',
                 'password1',
                 'password2',
                 'is_staff',
                 'is_active'
             )
         }),
    )
