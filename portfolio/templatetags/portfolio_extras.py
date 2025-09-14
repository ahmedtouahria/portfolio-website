from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given argument"""
    if value:
        return value.split(arg)
    return []

@register.filter
def trim(value):
    """Remove leading and trailing whitespace"""
    if value:
        return value.strip()
    return value

@register.filter
def slugify_custom(value):
    """Convert to lowercase and replace spaces with hyphens"""
    if value:
        return value.lower().replace(' ', '-').replace('&', 'and')
    return value