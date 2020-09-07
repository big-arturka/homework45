from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            errors.append(ValidationError("One of the fields (first_name, last_name) must be filled in."))
        if errors:
            raise ValidationError(errors)
        return cleaned_data
