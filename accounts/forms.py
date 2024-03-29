from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser

class UserLoginForm(AuthenticationForm):
    pass

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'age']
