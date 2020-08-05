from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Описание:')
    description = forms.CharField(max_length=200, required=False, label='Подробное описание:', widget=forms.Textarea)
    completion_date = forms.DateField(required=False, label='Дата завершения:', widget=forms.DateInput(attrs={'type':
                                                                                                              'date'}))
