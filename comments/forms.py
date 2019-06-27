from django import forms
from .models import Comment

#用来存放表单代码
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']