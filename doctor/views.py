from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from hospital.models import *
from patient.models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
# Create your views here.


def homeDoctor(request):

       return render(request, "doctorApp/home.html")

def myAppointmentDoctor(request):
       #getting Doctor ID
       doctorId = Doctor.objects.values_list('id', flat=True).get(userID_id=request.user.id)
       #getting all listid with doctor id
       listId =  list(List.objects.filter(doctor_id=doctorId).values('id','department_id','hospital_id','timeslot_id'))
       #getting booking list with same list id
       AllBookingList=[]
       for i in listId:
              item = BookingPatient.objects.filter(lists_id=i['id'])
              if(item.exists()): 
                     #getting all booking patient with same list id
                     bookinglist =list(item.values('state','appointmentDate','patient_id','lists_id').order_by('appointmentDate'))
                     AllBookingList.append(bookinglist)
                    
                     # timeslot = Timing.objects.values_list('timeslot', flat=True).get(id=i['timeslot_id'])
                     # print(bookinglist)
                     # print(list({hospitalName,departmentName,timeslot}))

       eachBookingList=[]
       for i in AllBookingList:
         for j in i:  
              patientUserId=Patient.objects.values_list('userID_id', flat=True).get(id=j['patient_id'])
              hospitalId=List.objects.values_list('hospital_id', flat=True).get(id=j['lists_id'])
              departmentId=List.objects.values_list('department_id', flat=True).get(id=j['lists_id'])
              timeslotId=List.objects.values_list('timeslot_id', flat=True).get(id=j['lists_id'])

              item ={'patientName':CustomUser.objects.values_list('first_name', flat=True).get(id=patientUserId),
                     'patientstate':j['state'],
                     'appointmentDate':str(j['appointmentDate']),
                     'hospitalName':Hospital.objects.values_list('name', flat=True).get(id=hospitalId),
                     'depName':Department.objects.values_list('name', flat=True).get(id=departmentId),
                     'timeslot':Timing.objects.values_list('timeslot', flat=True).get(id=timeslotId),
                            }
              eachBookingList.append(item) 
       
       context={'doctorId':doctorId , 'eachBookingList':json.dumps(eachBookingList)}

       return render(request, "doctorApp/myAppointments.html",context)


 
 

    