from django import forms

class EditPostForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128, error_messages={'required': '请输入文章标题'})
    tags = forms.CharField(label='标签', max_length=128, required=False)
    body = forms.CharField(label='内容', widget=forms.Textarea, error_messages={'required': '请输入文章内容'})

class CommentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=256, error_messages={'required': '请输入姓名'})
    url = forms.URLField(label='网站', required=False)
    email = forms.EmailField(label='邮件地址', error_messages={'required': '请输入email'})
    comment = forms.CharField(label='评论', widget=forms.Textarea, error_messages={'required': '请输入评论内容'})

class EditProfileForm(forms.Form):
    first_name = forms.CharField(label='名字', max_length=30)
    last_name = forms.CharField(label='姓氏', max_length=30)
    email = forms.EmailField(label='邮件地址')
