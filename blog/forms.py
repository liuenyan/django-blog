from django import forms
from .models import Category

class EditPostForm(forms.Form):
    title = forms.CharField(
        label='标题',
        max_length=128,
        error_messages={
            'required': '标题不能为空',
        },
        help_text='您的文章标题'
    )
    slug = forms.SlugField(
        label='缩略名',
        error_messages={
            'required': 'slug不能为空',
            'invalid': 'slug无效',
        },
        help_text='缩略名(slug)是文章标题的URL友好型版本'
    )
    tags = forms.CharField(
        label='标签',
        max_length=128,
        required=False,
        help_text='使用标签将更具体的关键字与您的文章关联起来'
    )
    categories = forms.ModelMultipleChoiceField(
        label='分类',
        queryset=Category.objects.all(),
        help_text='使用类别按主题对您的文章进行分组'
    )
    body_markdown = forms.CharField(
        label='内容',
        widget=forms.Textarea,
        error_messages={
            'required': '文章内容不能为空',
        },
        help_text='使用Markdown语法编辑文章'
    )


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
