from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path(
        "",
        views.task_list,
        name="task_list",
    ),

    path(
        "create/",
        views.task_create,
        name="task_create",
    ),

    path(
        "my-tasks/",
        views.my_tasks,
        name="my_tasks",
    ),

    path(
        "<int:pk>/",
        views.task_detail,
        name="task_detail",
    ),

    path(
        "<int:pk>/edit/",
        views.task_edit,
        name="task_edit",
    ),

    path(
        "<int:pk>/status/",
        views.update_task_status,
        name="update_task_status",
    ),

    path(
        "<int:pk>/comment/",
        views.add_comment,
        name="add_comment",
    ),
]