from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserRegister(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.PasswordInput()
    username = forms.CharField(max_length=30)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError('This username already exists in database')
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('One account, one email')
        return email
    
class UserLogin(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    def get_auth_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class ResetPassword(forms.Form):
    newpassword = forms.CharField(max_length=30)
    retypepassword = forms.CharField(max_length=30)

    def clean(self):
        data = self.cleaned_data
        newpassword = data.get('newpassword')
        retypepassword = data.get('retypepassword')
        if newpassword != retypepassword:
            raise forms.ValidationError('Passwords must be the same!')
        return data
