from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


class UserRegisstreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLogin(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user


class AuthenticateUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


### Custom Forms Without ModelForm  ###
# When creating a custom form that isn’t tied to a model, you define it using forms.Form.
# You can then define a save() method in the form class to process the data.
class ContactMailForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        # Extract cleaned data
        data = self.cleaned_data
        # Perform an operation, e.g., send an email
        send_mail(
            subject=f"Message from {data['name']}",
            message=data['message'],
            from_email=data['email'],
            recipient_list=['1322noobmaster@gmail.com'],
        )
