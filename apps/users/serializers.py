from rest_framework import serializers

from apps.tasks.models import TaskModel
from apps.users.models import User


class CreatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name',
                  'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskForUserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%H:%M   %d.%m.%Y")

    class Meta:
        model = TaskModel
        fields = [
            'name', 'description', 'created'
        ]


class CurrentUserSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = obj.tasks.all()
        serializer = TaskForUserSerializer(tasks, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name',
                  'tasks']
