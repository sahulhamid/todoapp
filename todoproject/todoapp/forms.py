from django import forms
from .models import TaskForm


class Task_Todo_Form(forms.ModelForm):
    class Meta:
        model = TaskForm
        fields = ['task', 'compeleted', 'date']
