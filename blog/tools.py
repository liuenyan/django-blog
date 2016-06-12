from django.contrib.auth.models import User
from faker import Factory
import bleach
from bleach_whitelist import generally_xss_safe
from .models import Post, Comment

def generate_fake_posts(nums=50):
    fake = Factory.create('en_US')
    for _ in range(nums):
        post = Post(
            title=fake.word(),
            body=fake.paragraph(),
            author=User.objects.get(pk=2)
        )
        post.save()
        generate_fake_comments(post)


def generate_fake_comments(post, nums=10):
    fake = Factory.create('en_US')
    for _ in range(nums):
        comment = Comment(
            name=fake.name(),
            email=fake.email(),
            url=fake.url(),
            comment=fake.paragraph(),
            post=post
        )
        comment.save()

def clean_html_tags(data):
    return bleach.linkify(bleach.clean(data, generally_xss_safe), skip_pre=True)
