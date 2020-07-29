from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password1', 'password2']