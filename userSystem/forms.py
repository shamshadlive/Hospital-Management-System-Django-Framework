from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


#User Registration form - creating basic user model
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','first_name','email','password1','password2','phone_number','user_Type']

#User Profile pic section
class CustomUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['profilepic',]
        labels = {
            'profilepic': '<i class="bi bi-pencil-fill"></i> Click here to Update Profile Pic',
        }
 
                
                