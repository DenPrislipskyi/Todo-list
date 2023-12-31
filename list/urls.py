from django.urls import path

from list.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView,
                        change_is_done)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/change-is-done/", change_is_done, name="change-is-done"),
]

app_name = "list"
