from django.urls import path

from list.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/creata", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "list"
