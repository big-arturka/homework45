from django import forms

from webapp.models import Status, Task_type


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Название:',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=2000, required=False, label='Подробное описание:',
                                  widget=forms.Textarea(attrs={'class': 'form-area'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус:', empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    type = forms.ModelChoiceField(queryset=Task_type.objects.all(), required=True, label='Тип:', empty_label=None,
                                  widget=forms.Select(attrs={'class': 'form-select'}))
