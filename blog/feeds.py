"""
这个文件定义了RSS输出。
"""
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from blog.models import Post

class PostFeed(Feed):
    """
    定义文章 ATOM 输出的类
    """
    feed_type = Atom1Feed
    title = "学习笔记"
    link = "/"
    subtitle = "恩岩的学习笔记"

    def items(self):
        return Post.objects.order_by('-id')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_html
