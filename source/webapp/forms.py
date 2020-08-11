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

    #
    # title = forms.CharField(max_length=200, required=True, label='Название:',
    #                         widget=forms.TextInput(attrs={'class': 'form-input'}))
    # description = forms.CharField(max_length=2000, required=False, label='Подробное описание:',
    #                               widget=forms.Textarea(attrs={'class': 'form-area'}))
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус:', empty_label=None,
    #                                 widget=forms.Select(attrs={'class': 'form-select'}))
    # type = forms.ModelMultipleChoiceField(queryset=Task_type.objects.all(), required=True, label='Тип:',
    #                                       widget=forms.CheckboxSelectMultiple(attrs={'class': 'radio-btn'}))
