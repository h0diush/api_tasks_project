from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TagModel, TaskModel
from .serializers import CreatedTaskSerializer, TagCreatedSerializer, \
    TagListSerializer, UserTaskListSerializer
from ..users.permissions import UpdateTaskPermissions


class TaskListViewSet(viewsets.ModelViewSet):
    serializer_class = UserTaskListSerializer
    permission_classes = [permissions.IsAuthenticated, UpdateTaskPermissions]

    def get_serializer_class(self):
        if self.action == 'created_tag':
            return TagCreatedSerializer
        if self.request.method == 'GET':
            return UserTaskListSerializer
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return CreatedTaskSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['POST'])
    def created_tag(self, request):
        name = request.POST.get('name')
        tag = TagModel.objects.create(
            name=name,
            author=request.user
        )
        tag.save()
        return Response('message Тег успешно добавлен',
                        status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def my_tag_list(self, request):
        tags = request.user.tags.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data)

    # TODO добавить action method создания tasks

    def get_queryset(self):
        user = self.request.user.username
        tasks = TaskModel.objects.filter(author__username=user)
        return tasks

    # TODO добавить поле создания Тегов
