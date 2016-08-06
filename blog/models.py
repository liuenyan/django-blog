"""
这个文件定义 blog 应用的数据模型。
"""
from django.db import models
from django.contrib.sitemaps import ping_google

# Create your models here.

class Tag(models.Model):
    """标签的数据模型"""
    tag = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.tag


class Category(models.Model):
    """分类的数据模型"""
    category = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    """文章的数据模型"""
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    body_markdown = models.TextField()
    body_html = models.TextField()
    author = models.ForeignKey('auth.User')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Post, self).save(force_insert, force_update, using, update_fields)
        try:
            ping_google()
        except Exception:
            pass

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('post', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    """评论的数据模型"""
    name = models.CharField(max_length=256)
    email = models.EmailField()
    url = models.URLField(blank=True)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post')

    def __str__(self):
        return self.comment


class Link(models.Model):
    """链接的数据模型"""
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    link = models.URLField()

    def __str__(self):
        return self.name
