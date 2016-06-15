from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from .models import Post

class PostFeed(Feed):
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
