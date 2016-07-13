from django.contrib.sitemaps import Sitemap
from .models import Post

class StaticSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['index', ]

    def location(self, item):
        from django.core.urlresolvers import reverse
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modification_time
