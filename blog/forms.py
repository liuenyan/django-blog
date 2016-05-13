from django import forms

class EditPostForm(forms.Form):
    title = forms.CharField(label=u"标题", max_length=128)
    tags = forms.CharField(label=u'标签', max_length=128, required=False)
    body = forms.CharField(label=u'内容', widget=forms.Textarea)


class CommentForm(forms.Form):
    name = forms.CharField(label=u'姓名', max_length=256)
    url = forms.URLField(label=u'网站')
    email = forms.EmailField(label=u'邮件地址')
    comment = forms.CharField(label=u'评论', widget=forms.Textarea)

