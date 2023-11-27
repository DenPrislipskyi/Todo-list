from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TaskForm
from list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list/task_delete.html"
    success_url = reverse_lazy("list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "list/tag_form.html"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "list/tag_form.html"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "list/tag_delete.html"
    success_url = reverse_lazy("list:tag-list")
