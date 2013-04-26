from django import template

register = template.Library()

@register.simple_tag(name = 'hello')
def hello():
    value = 'Hello World!'
    return value