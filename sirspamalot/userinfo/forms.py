from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import SpamMessage, Profile
from django.contrib.auth.models import User
#from . import views

class SpamMessageForm(forms.ModelForm):
    spam_message = forms.CharField(max_length=140)
    
    class Meta:
        model = SpamMessage
        fields = ('spam_message',)


class LoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



