
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('home-hospital', views.homeHospital, name='homeHospital'),
    path('changeStatusHospital', views.changeStatusHospital, name='changeStatusHospital'),
    path('addHospital', views.addHospital, name='addHospital'),




]
 