from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userregisterform(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta :
        model = User
        fields = ("username", "email", "password1", "password2")

class userupdateform(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")