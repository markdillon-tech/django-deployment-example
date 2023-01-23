from django import template

register = template.Library()

@register.filter(name='kut')
def cut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
