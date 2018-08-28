from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    """Form to be used to log users in"""

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))    
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2
   