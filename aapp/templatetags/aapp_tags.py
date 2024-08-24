from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()

@register.simple_tag(name='lastposts')
def aapp_lastposts():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())[:2]
    return posts