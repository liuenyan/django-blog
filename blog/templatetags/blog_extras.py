from django import template
from ..models import Post, Tag, Link
from django.db.models import Count
import hashlib

register = template.Library()

@register.inclusion_tag('_sidebar.html')
def show_sidebar():
    tags = Tag.objects.all()
    archives = Post.objects.extra(select={'year': 'strftime("%Y", timestamp)', 'month': 'strftime("%m", timestamp)'}).values('year', 'month').annotate(Count('id'))
    links = Link.objects.all()
    return {'tags': tags, 'archives': archives, 'links': links}

@register.filter
def gravatar(email, size=60, default='identicon'):
    md5 = hashlib.md5(email.encode('utf8').lower()).hexdigest()
    gravatar_url = "//cdn.v2ex.com/gravatar/{0}?s={1}&d={2}".format(md5, str(size), default)
    return gravatar_url
