from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """_summary_
    Class BlogForm
    """
    class Meta:
        """_summary_
        """
        model = Blog
        fields = ['title', 'content', 'is_published']  # Include fields you want in the form
