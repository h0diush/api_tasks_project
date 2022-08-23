from django.core.exceptions import ValidationError

CODE_PHONE = ['44', '29', '33', '25']


def validate_phone(phone):
    if not phone.isdigit():
        raise ValidationError('Номер должен состоять из цифр')
    if len(phone) < 9:
        raise ValidationError('Номер должен состоять из 9 цифр')
    if len(phone) > 9:
        raise ValidationError('Номер должен состоять из 9 цифр')
    if phone[0:2] not in CODE_PHONE:
        raise ValidationError(
            f'Проверьте коды операторов'
            f'{", ".join(_ for _ in CODE_PHONE)}'
        )
    return phone
