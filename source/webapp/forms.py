from django import forms
from webapp.models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'task_type']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'description': forms.Textarea(attrs={'class': 'form-area'}),
                   'status': forms.Select(attrs={'class': 'form-select'}),
                   'task_type': forms.CheckboxSelectMultiple(attrs={'class': 'radio-btn'})
                   }


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-input'}),
                   'description': forms.Textarea(attrs={'class': 'form-area'}),
                   'start_date': forms.SelectDateWidget(attrs={'class': 'date-form'}),
                   'end_date': forms.SelectDateWidget(attrs={'class': 'date-form'}),
                   }


class ProjectUsersForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['user']
        widgets = {'user': forms.CheckboxSelectMultiple(attrs={'class': 'radio-btn'})
                   }