from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def endswith(text, postfix):
    return text.endswith(postfix)


@register.filter
@stringfilter
def startswith(text, prefix):
    return text.startswith(prefix)