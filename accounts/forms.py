from django import forms

class UserloginForm(forms.Form):
    """Form for user to input login details"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)