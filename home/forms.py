from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254,required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )