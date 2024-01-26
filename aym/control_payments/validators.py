from django.core.exceptions import ValidationError
from datetime import date


def validate_cpf(value):
    if len(value) != 11:
        raise ValidationError("CPF must have 11 digits")
    product_sum_1 = sum(int(a) * int(b) for a, b in zip(value[0:9], range(10, 1, -1)))
    digit_1 = (product_sum_1 * 10 % 11) % 10
    product_sum_2 = sum(int(a) * int(b) for a, b in zip(value[0:10], range(11, 1, -1)))
    digit_2 = (product_sum_2 * 10 % 11) % 10
    if int(value[9]) != digit_1 or int(value[10]) != digit_2:
        raise ValidationError("CPF is invalid")


def validate_birth_date(value):
    if value > date.today():
        raise ValidationError("Birth date can't be in the future")
