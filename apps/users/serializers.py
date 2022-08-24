from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.tasks.models import TagModel, TaskModel
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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['name']


class TaskForUserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%H:%M %d.%m.%Y")
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_tags(obj):
        tags = obj.tags.all()
        serializer = TagSerializer(tags, many=True)
        return serializer.data

    class Meta:
        model = TaskModel
        fields = [
            'name', 'description', 'created', 'tags'
        ]


class CurrentUserSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    @staticmethod
    def get_tasks(obj):
        tasks = obj.tasks.all()
        serializer = TaskForUserSerializer(tasks, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name',
                  'tasks']


class TokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        token['created'] = f'{user.date_joined.strftime("%H:%M  %d.%b.%Y")}'
        return token
