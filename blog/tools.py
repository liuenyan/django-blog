from .models import Post, Tag, Comment
from django.contrib.auth.models import User
from functools import reduce
from faker import Factory


def generate_fake_posts(nums=50):
    fake = Factory.create('en_US')
    for i in range(nums):
        post = Post(title = fake.word(), body=fake.paragraph(), author=User.objects.get(pk=2))
        post.save()
        generate_fake_comment(post)


def generate_fake_comment(post, nums=10):
    fake = Factory.create('en_US')
    for i in range(10):
        comment = Comment(name=fake.name(), email=fake.email(), url=fake.url(), comment=fake.paragraph(), post=post)
        comment.save()
