"""
定义站点地图。
"""
from django.contrib.sitemaps import Sitemap
from blog.models import Post

class StaticSitemap(Sitemap):
    """静态链接的站点地图"""
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['index', ]

    def location(self, item):
        from django.core.urlresolvers import reverse
        return reverse(item)

class PostSitemap(Sitemap):
    """文章详情页面的站点地图"""
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modification_time
