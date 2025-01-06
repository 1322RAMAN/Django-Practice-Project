from django import forms
from .models import CustomUser


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')


# class SuperuserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_staff = True
#         user.is_superuser = True
#         if commit:
#             user.save()
#         return user


# class AuthenticateUserForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)


# ### Custom Forms Without ModelForm  ###
# # When creating a custom form that isn’t tied to a model, you define it using forms.Form.
# # You can then define a save() method in the form class to process the data.
# class ContactMailForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

#     def save(self):
#         # Extract cleaned data
#         data = self.cleaned_data
#         # Perform an operation, e.g., send an email
#         send_mail(
#             subject=f"Message from {data['name']}",
#             message=data['message'],
#             from_email=data['email'],
#             recipient_list=['1322noobmaster@gmail.com'],
#         )
