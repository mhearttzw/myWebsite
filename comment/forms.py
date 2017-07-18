
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # 内部类
    class Meta:
        # 对应的数据库模型
        model = Comment
        fields = ['name', 'email', 'url', 'text']
