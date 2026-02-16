from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import List, Task
from .forms import ListForm, TaskForm


class ListListView(ListView):
    model = List
    template_name = "main/list_list.html"
    context_object_name = "lists"


class ListDetailView(DetailView):
    model = List
    template_name = "main/list_detail.html"
    context_object_name = "list"


class ListCreateView(CreateView):
    model = List
    form_class = ListForm
    template_name = "main/list_form.html"
    success_url = reverse_lazy('list-list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "main/task_form.html"
    success_url = reverse_lazy('list-list')

from django.views.generic import DeleteView
class ListDeleteView(DeleteView):
    model = List
    template_name = "main/list_confirm_delete.html"
    success_url = reverse_lazy('list-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "main/task_confirm_delete.html"
    success_url = reverse_lazy('list-list')
