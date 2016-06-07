from django import forms

class EditPostForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128)
    tags = forms.CharField(label='标签', max_length=128, required=False)
    body = forms.CharField(label='内容', widget=forms.Textarea)

class CommentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=256)
    url = forms.URLField(label='网站', required=False)
    email = forms.EmailField(label='邮件地址')
    comment = forms.CharField(label='评论', widget=forms.Textarea)

class EditProfileForm(forms.Form):
    first_name = forms.CharField(label='名字', max_length=30)
    last_name = forms.CharField(label='姓氏', max_length=30)
    email = forms.EmailField(label='邮件地址')
