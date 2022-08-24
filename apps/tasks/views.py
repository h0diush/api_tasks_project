from rest_framework import viewsets, permissions

from .models import TaskModel
from .serializers import UserTaskListSerializer, CreatedTaskSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    serializer_class = UserTaskListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserTaskListSerializer
        if self.request.method == 'POST':
            return CreatedTaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # TODO добавить action method создания tasks

    def get_queryset(self):
        user = self.request.user.username
        tasks = TaskModel.objects.filter(author__username=user)
        return tasks

    # TODO добавить поле создания Тегов