from rest_framework import serializers

from apps.services.utils import get_tags_for_tasks
from apps.tasks.models import TagModel, TaskModel
from apps.users.serializers import TagSerializer


class UserTaskListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%H:%M %d.%m.%Y",
                                        read_only=True)

    @staticmethod
    def get_tags(obj):
        return get_tags_for_tasks(obj, TagSerializer)

    # def create(self, validated_data):
    #     tags_data = validated_data.pop(tags)

    class Meta:
        model = TaskModel
        fields = [
            'name', 'description', 'created', 'tags'
        ]


class CreatedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            'name', 'description', 'tags'
        ]


class TagCreatedSerializer(serializers.Serializer):
    name = serializers.CharField(label='Название тега')


class TagListSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%H:%M %d.%m.%Y")

    class Meta:
        model = TagModel
        fields = [
            'name', 'created'
        ]
