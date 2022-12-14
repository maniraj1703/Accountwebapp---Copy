from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class SigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
