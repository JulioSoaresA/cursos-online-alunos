from django import template

register = template.Library()


@register.filter(name='plus_one')
def plus_one(value):
    try:
        return int(value + 1)
    except:
        return None
