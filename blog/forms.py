from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Category, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'categories', 'tags', 'body_markdown']
        widgets = {
            'categories': CheckboxSelectMultiple,
            'tags': CheckboxSelectMultiple,
        }
        labels = {
            'title': '标题',
            'slug': '缩略名',
            'categories': '分类',
            'tags': '标签',
            'body_markdown': '内容',
        }
        help_texts = {
            'title': '您的文章标题',
            'slug': '缩略名(slug)是文章标题的URL友好型版本',
            'tags': '使用标签将更具体的关键字与您的文章关联起来',
            'categories': '使用类别按主题对您的文章进行分组',
            'body_markdown': '使用Markdown语法编辑文章',
        }
        error_messages = {
            'title': {
                'required': '标题不能为空',
            },
            'slug': {
                'required': 'slug不能为空',
                'invalid': 'slug无效',
            },
            'body_markdown': {
                'required': '文章内容不能为空',
            },
        }


class CommentForm(forms.Form):
    name = forms.CharField(
        label='姓名',
        max_length=256,
        error_messages={
            'required': '姓名不能为空',
        }
    )
    url = forms.URLField(
        label='网站',
        required=False
    )
    email = forms.EmailField(
        label='邮件地址',
        error_messages={
            'required': 'email不能为空',
        }
    )
    comment = forms.CharField(
        label='评论',
        widget=forms.Textarea,
        error_messages={
            'required': '评论内容不能为空',
        }
    )


class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        label='名字',
        max_length=30
    )
    last_name = forms.CharField(
        label='姓氏',
        max_length=30
    )
    email = forms.EmailField(label='邮件地址')
