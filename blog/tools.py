"""
这个文件定义了一些有用的工具函数。
"""
import bleach
import markdown
from bleach_whitelist import generally_xss_safe
from blog.models import Post, Comment

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
