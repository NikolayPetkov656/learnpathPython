from django import template


register = template.Library()


@register.filter
def completion_label(value):
    return "Completed" if value else "To do"