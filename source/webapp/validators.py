from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


def descriptions_validator(string):
    curse_words = ['fuck', 'ass', 'bitch', 'idiot']
    for word in curse_words:
        if word in string:
            raise ValidationError('The text contains obscene words, obscene language is prohibited!!!')


def name_char(string):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for char in string:
        if char in nums:
            raise ValidationError('This field cannot contain characters.')