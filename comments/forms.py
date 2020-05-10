__author__ = 'Luguaa'
__date__ = '2020/5/8 16:09'

from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'url', 'text']
