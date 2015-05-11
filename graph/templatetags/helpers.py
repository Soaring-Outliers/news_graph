from django import template
import bleach

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

register = template.Library()
    
@register.filter
def sanitize(text):
    ALLOWED_TAGS = ['p', 'span', 'h5', 'h6']
    ALLOWED_ATTRIBUTES = []
    ALLOWED_STYLES = []
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
        styles=ALLOWED_STYLES, strip=True, strip_comments=True)

@register.filter
def log(text):
    logger.error(text)