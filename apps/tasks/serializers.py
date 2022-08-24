from rest_framework import serializers

from apps.tasks.models import TaskModel
from apps.users.serializers import TagSerializer


class UserTaskListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%H:%M %d.%m.%Y",
                                        read_only=True)

    @staticmethod
    def get_tags(obj):
        tags = obj.tags.all()
        serializer = TagSerializer(tags, many=True)
        return serializer.data

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
