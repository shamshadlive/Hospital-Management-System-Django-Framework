
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('home-hospital', views.homeHospital, name='homeHospital'),
    path('changeStatusHospital', views.changeStatusHospital, name='changeStatusHospital'),
    path('hospitalview/changeStatusHospitalDoctor', views.changeStatusHospitalDoctor, name='changeStatusHospitalDoctor'),
    path('addHospital', views.addHospital, name='addHospital'),
    path('hospitalDelete/<int:id>', views.hospitalDelete, name='hospitalDelete'),
    path('hospitalview/<str:getname>', views.hospitalview, name='hospitalview'),
    path('hosadmin/profile', views.hosadminMyProfile, name='hosadminMyProfile'),
    #profile pic update
    path('uploadHosAdminPropic/<int:id>', views.uploadHosAdminPropic, name='uploadHosAdminPropic'),

    #add new doctor
     path('addDoctor/<int:id>', views.addDoctor, name='addDoctor'),
    




]
 