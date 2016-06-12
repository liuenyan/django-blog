import hashlib
from django import template
from django.db.models import Count
from ..models import Post, Tag, Link

register = template.Library()

@register.inclusion_tag('_navbar.html')
def show_navbar(active, user):
    return {'active': active, 'user': user}

@register.inclusion_tag('_sidebar.html')
def show_sidebar():
    tags = Tag.objects.annotate(Count('post')).filter(post__count__gt=0).order_by('tag')
    archives = Post.objects.extra(select={
        'year': 'strftime("%Y", timestamp)',
        'month': 'strftime("%m", timestamp)'
    }).values('year', 'month').annotate(Count('id')).order_by('-year', '-month')
    links = Link.objects.all()
    return {'tags': tags, 'archives': archives, 'links': links}

@register.filter
def gravatar(email, size=60, default='identicon'):
    md5 = hashlib.md5(email.encode('utf8').lower()).hexdigest()
    gravatar_url = "//cdn.v2ex.com/gravatar/{0}?s={1}&d={2}".format(md5, str(size), default)
    return gravatar_url

@register.filter
def alert_class(level_tag):
    if level_tag == 'error':
        return 'alert-danger'
    elif level_tag in ['info', 'success', 'warning']:
        return 'alert-{0}'.format(level_tag)
    else:
        return 'alert-info'
