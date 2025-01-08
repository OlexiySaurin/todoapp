from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/update/", views.task_update, name="task-update"),
    path("task/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("task/create/", views.task_create, name="task-create"),
    path("task/<int:pk>/toggle_complete/", views.toggle_complete, name="toggle-complete"),
]