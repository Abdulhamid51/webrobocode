from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","first_name",'last_name', "email", "password1", "password2"]
        widgets = {}

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['job','birth','place','phone','python','php','js','java','c','edu','work','bio']