from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserloginForm(forms.Form):
    """Form for user to input login details"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """Frorm is used to register the user"""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget = forms.PasswordInput)

    class Meta: # Inner class is used by Djano to provide infomation about the forms.
        model = User # Specifies the name of the model where we want to store user information
        fields = ['email', 'username', 'password1', 'password2']