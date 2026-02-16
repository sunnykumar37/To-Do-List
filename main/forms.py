from django import forms
from .models import List, Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['list', 'title', 'description', 'is_completed']
