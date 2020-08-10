from django.template import Library
from stories.models import Comments


register=Library()

@register.filter
def replies(msg):
    reply=Comments.objects.filter(parent_msg=msg)
    return reply