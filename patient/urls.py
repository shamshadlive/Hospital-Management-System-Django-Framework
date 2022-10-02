
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('home-patient', views.homePatient, name='homePatient'),
    path('login-patient', views.loginPatient, name='loginPatient'),
    path('register-patient', views.registerPatient, name='registerPatient'),
    path('resetPassword-patient', views.resetPasswordPatient, name='resetPasswordPatient'),

]
 