"""
这个文件定义了一些有用的工具函数。
"""
import bleach
import markdown
from django.contrib.auth.models import User
from faker import Factory
from bleach_whitelist import generally_xss_safe
from blog.models import Post, Comment

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
    return bleach.linkify(
        bleach.clean(data, generally_xss_safe),
        skip_pre=True
    )

def convert_to_html(markdown_text):
    md = markdown.Markdown(
        extensions=[
            'pymdownx.github',
            'markdown.extensions.toc',
        ],
        extension_configs={
            'markdown.extensions.toc':
            {
                'title': '目录',
            },
        },
        output_format="html5"
    )
    return md.convert(markdown_text)
