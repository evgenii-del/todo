from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for task model
    """

    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ("id", "owner", "content", "created_at", "is_done", "is_priority")
        read_only_fields = ("is_done", "is_priority")
