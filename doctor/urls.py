
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('home-doctor', views.homeDoctor, name='homeDoctor'),

]
 