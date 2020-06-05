from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="task")
    created_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    is_priority = models.BooleanField(default=False)

    class Meta:
        ordering = ("is_done", "-is_priority", "-created_at")
