from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

userChoices = (
        ('HOSADMIN', 'Hospital Admin'),
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
    )



class CustomUser(AbstractUser):
    phone_number= models.CharField(null=True, blank=True,max_length=10)
    user_Type = models.CharField(max_length=10, choices=userChoices,default='NULL')

#setting email field unique
CustomUser._meta.get_field('email')._unique = True

