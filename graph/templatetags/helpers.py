from django import template
import bleach

register = template.Library()
    
@register.filter
def sanitize(text):
    ALLOWED_TAGS = ['p', 'span', 'h5', 'h6']
    ALLOWED_ATTRIBUTES = []
    ALLOWED_STYLES = []
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
        styles=ALLOWED_STYLES, strip=True, strip_comments=True)