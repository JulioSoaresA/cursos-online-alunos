from django.core.exceptions import ValidationError


def file_size(value):
    limit = 1048576
    if value.size > limit:
        raise ValidationError('Arquivo muito grande. Tamanho máximo: 1MB')
