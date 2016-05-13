from django import template
from ..models import Post, Tag
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('_sidebar.html')
def show_sidebar():
    tags = Tag.objects.all()
    archives = Post.objects.extra(select={'year': 'strftime("%Y", timestamp)', 'month': 'strftime("%m", timestamp)'}).values('year', 'month').annotate(Count('id'))
    return {'tags': tags, 'archives': archives}