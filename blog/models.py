from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    url = models.URLField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post')

    def __str__(self):
        return self.comment



