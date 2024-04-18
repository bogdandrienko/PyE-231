from django import template
from django.http import HttpRequest

register = template.Library()


@register.filter(name="capitalize_string")
def capitalize_string(value: str):
    return str(value).capitalize()


@register.simple_tag(takes_context=True)
def text_slice(context, text: str, length: int):
    request: HttpRequest = context["request"]
    return str(text)[:length]
