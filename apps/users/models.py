from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager
from .validators import validate_phone


class User(AbstractUser):
    username = models.CharField('Имя пользователя', unique=True, null=True,
                                blank=True, max_length=25)
    email = models.EmailField('Электронная почта', unique=True)
    first_name = models.CharField('Имя', max_length=55)
    last_name = models.CharField('Фамилия', max_length=55)
    phone = models.CharField('Номер телефона', max_length=13,
                             validators=[validate_phone], null=True,
                             blank=True, help_text='+375XXXXXXXXX')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.last_name} {self.first_name}'
        return self.username

    def get_phone(self):
        return f'+375{self.phone}'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
