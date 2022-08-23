from django.db import models

from apps.users.models import User


class TaskModel(models.Model):
    name = models.CharField('Название', max_length=75)
    description = models.TextField('Описание', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Автор',
                               related_name='tasks',
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField('TagModel', verbose_name='Тэг', null=True,
                                 blank=True, related_name='tasks')
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


class TagModel(models.Model):
    name = models.CharField('Название', max_length=55)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Автор',
                               related_name='tags',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name
