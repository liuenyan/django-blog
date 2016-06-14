from django.db import models
from django.contrib.sitemaps import ping_google

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=128)
    body_markdown = models.TextField()
    body_html = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
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
        return reverse('post', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    url = models.URLField(blank=True)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post')

    def __str__(self):
        return self.comment


class Link(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    link = models.URLField()

    def __str__(self):
        return self.name

