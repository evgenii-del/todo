from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin):
    """
    ViewSet to work with to-do list.
    Methods implemented: create a task, delete a task,
    cancel the task as a priority, сancel the task as completed.
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(owner=user)
        return queryset

    @action(detail=True, methods=["patch"])
    def done(self, *args, **kwargs):
        task = Task.objects.filter(pk=kwargs["pk"])

        if task[0].is_done:
            task.update(is_done=False)
        else:
            task.update(is_done=True)
            task.update(is_priority=False)

        return Response(status=201)

    @action(detail=True, methods=["patch"])
    def priority(self, *args, **kwargs):
        task = Task.objects.filter(pk=kwargs["pk"])

        if task[0].is_priority:
            task.update(is_priority=False)
        else:
            task.update(is_priority=True)
            task.update(is_done=False)

        return Response(status=201)
