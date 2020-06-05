from django.urls import path

from .views import TaskViewSet

task_list = TaskViewSet.as_view({"get": "list", "post": "create"})

task_detail = TaskViewSet.as_view({"delete": "destroy"})

task_done = TaskViewSet.as_view({"patch": "change_done"})

task_priority = TaskViewSet.as_view({"patch": "change_priority"})

urlpatterns = [
    path("tasks/", task_list),
    path("tasks/<int:pk>/delete/", task_detail),
    path("tasks/<int:pk>/done/", task_done),
    path("tasks/<int:pk>/priority/", task_priority),
]
