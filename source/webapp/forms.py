from django import forms
from webapp.models import Status, Task_type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'task_type']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'description': forms.Textarea(attrs={'class': 'form-area'}),
                   'status': forms.Select(attrs={'class': 'form-select'}),
                   'task_type': forms.CheckboxSelectMultiple(attrs={'class': 'radio-btn'})}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")