from django.contrib import admin
from .models import TagModel, TaskModel


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_filter = ['created']
    list_display = ['name', 'created', 'get_author']
    list_display_links = ['name']
    exclude = ['tags']

    def get_author(self, obj):
        return obj.author.username

    get_author.short_description = 'Автор'


class TagInline(admin.TabularInline):
    model = TaskModel.tags.through
    max_num = 3


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'get_author']
    list_filter = ['author', 'created']
    inlines = [TagInline]

    def get_author(self, obj):
        return obj.author.username

    get_author.short_description = 'Автор'
