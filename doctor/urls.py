
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('home-doctor', views.homeDoctor, name='homeDoctor'),
    path('doctor/myappointments', views.myAppointmentDoctor, name='myAppointmentDoctor'),
    path('doctor/profile', views.doctorMyProfile, name='doctorMyProfile'),
    path('uploadDoctorPropic/<int:id>', views.uploadDoctorPropic, name='uploadDoctorPropic'),
    #real url
    path('doctor/myappointments/change/markCompleted/<int:id>', views.doctorMarkCompeleted, name='doctorMarkCompeleted'),

     # url for mark pending
    path('doctor/myappointments/change/markPending/<int:id>', views.doctorMarkPending, name='doctorMarkPending'),

    #url for mark deleted
    path('doctor/myappointments/change/markDeleted/<int:id>', views.doctorMarkDeleted, name='doctorMarkDeleted'),

    #DOCUMENT UPLOADED DELETE
    path('doctor/myappointments/change/documentremove/<int:id>', views.doctordocumentDelete, name='doctordocumentDelete'),
   
]
