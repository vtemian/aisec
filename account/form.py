from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from account.models import UserProfile


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

class ProfileForm(ModelForm):

  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    try:
      self.fields['email'].initial = self.instance.user.email
      self.fields['first_name'].initial = self.instance.user.first_name
      self.fields['last_name'].initial = self.instance.user.last_name
    except User.DoesNotExist:
      pass

  email = forms.EmailField(label="Email",help_text='')
  first_name = forms.CharField(label="First name",help_text='')
  last_name = forms.CharField(label="Last name",help_text='')

  class Meta:
    model = UserProfile
    exclude = ('user',)

  def save(self, *args, **kwargs):
    """
    Update the primary email address on the related User object as well.
    """
    u = self.instance.user
    u.email = self.cleaned_data['email']
    u.save()
    profile = super(ProfileForm, self).save(*args,**kwargs)
    return profile

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
