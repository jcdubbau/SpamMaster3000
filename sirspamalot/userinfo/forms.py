from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import SpamMessage, Profile
from django.contrib.auth.models import User

class SpamMessageForm(forms.ModelForm):
    spam_messages = forms.CharField(max_length=140)
    
    class Meta:
        model = SpamMessage
        fields = ('spam_message',)


class LoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2',)


    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')

        return cd['password2']



