from django.core.exceptions import ValidationError


def file_size(value):
    filesize = value.size
    limit = 1048576
    if filesize >= limit:
        raise ValidationError('Arquivo muito grande. Tamanho máximo: 1MB')
