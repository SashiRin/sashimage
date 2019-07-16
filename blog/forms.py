from django import forms
from .models import Post
from markdownx.widgets import MarkdownxWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': MarkdownxWidget(attrs={'class': 'textarea'}),
        }
