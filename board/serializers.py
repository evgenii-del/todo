from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "owner", "content", "created_at", "is_done", "is_priority")
        read_only_fields = ("owner", "is_done", "is_priority")
