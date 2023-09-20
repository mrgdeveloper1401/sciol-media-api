from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'username', 'mobile')
        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError('this email already exists')
    #     return email

        
        
class UserSigninForm(AuthenticationForm):
    ...
        
        
# class RegisterUserForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput)    
#     password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('email', 'username', )
        
#         error_message = {
#             'email': {
#                 'required': 'please enter email address'
#             },
#             'password': {
#                 'required': 'please enter password'
#             },
#             'password2': {
#                 'required': 'please enter confirm password'
#             }
#         }
        
#     def clean(self):
#         cd = super().clean()
#         password = cd.get('password1')
#         password2 = cd.get('password2')
#         if password and password2 and password != password2:
#             raise ValidationError('password must be the same')
        
#     def clean_email(self):
#         cd = self.cleaned_data
#         if User.objects.filter(email=cd['email']).exists():
#             raise ValidationError('this email is already in exisits')
#         return cd['email']
    
#     def clean_username(self):
#         cd = self.cleaned_data
#         if User.objects.filter(username=cd['username']).exists():
#             raise ValidationError('this username is already in exisits')
#         return cd['username']