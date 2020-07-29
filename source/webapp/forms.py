from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Описание')
    description = forms.CharField(max_length=200, required=False, label='Подробное описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, label=default_status, initial='Статус')
    completion_date = forms.DateField(required=False, label='Дата завершения', widget=forms.DateInput(attrs={'type':
                                                                                                             'date'}))
