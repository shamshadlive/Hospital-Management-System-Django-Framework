
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('patient-home', views.homePatient, name='homePatient'),
    path('patient/newbooking', views.patientNewbooking, name='patientNewbooking'),
    path('patient/newbooking/choose-doctor', views.patientChooseDoctor, name='patientChooseDoctor'),
    path('getHospitalDepartment', views.getHospitalDepartment, name='getHospitalDepartment'),
    path('patientSaveBooking/<str:dep>/<str:hosname>/<str:uhid>', views.patientSaveBooking, name='patientSaveBooking'),
    path('patient-home/profile/mybooking', views.patientViewBooking, name='patientViewBooking'),
    path('patient/profile/myprofile', views.patientMyProfile, name='patientMyProfile'),


]
 