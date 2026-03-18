from urllib.parse import urlparse

from django import template

register = template.Library()

ABSOLUTE_SCHEMES = {"http", "https"}


@register.filter
def asset_url(value):
    if not value:
        return ""
    value = str(value).strip()
    parsed = urlparse(value)
    if parsed.scheme in ABSOLUTE_SCHEMES:
        return value
    if value.startswith("//"):
        return value
    if value.startswith("/"):
        return value
    return f"/{value.lstrip('/')}"
