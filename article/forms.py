from django.forms import ModelForm
from django import forms
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # Send email logic here
        pass


class ContactAuthorForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
