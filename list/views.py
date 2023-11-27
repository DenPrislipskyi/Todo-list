from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list/task_delete.html"
    success_url = reverse_lazy("list:task-list")

