from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doctor
from hospital.models import *
from patient.models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from hospital.forms import BookingPatientForm
from hospital.models import BookingPatient
from django.contrib.auth.decorators import login_required
from userSystem.forms import CustomUserProfileForm

# Create your views here.


@login_required(login_url='UserLogin')
def homeDoctor(request):

       return render(request, "doctorApp/home.html")

@login_required(login_url='UserLogin')
def myAppointmentDoctor(request):
       #file upload sectiom
       if request.method == "POST":
              bkTableToken=request.POST['bkTableToken']
              a = BookingPatient.objects.get(pk=bkTableToken)
              form = BookingPatientForm(request.POST, request.FILES,instance=a)
              if form.is_valid():
                     form.save()
              return redirect("myAppointmentDoctor")
       form = BookingPatientForm()

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
                     bookinglist =list(item.values('id','state','appointmentDate','patient_id','lists_id','documents').order_by('appointmentDate'))
                     AllBookingList.append(bookinglist)

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
                     'bkTableToken':j['id'],
                     'documents':j['documents']
                            }
              eachBookingList.append(item) 
       
      


       context={'form':form,'doctorId':doctorId , 'eachBookingList':eachBookingList}

       return render(request, "doctorApp/myAppointments.html",context)



#Doctor Profile 
#Redirect unauthorized user's from accessing 
@login_required(login_url='UserLogin')
def doctorMyProfile(request):


    #profile pic
    formset = CustomUserProfileForm()
    context={'formset':formset,}

    return render(request, 'doctorApp/myprofile.html',context)
    
#user pro pic
def uploadDoctorPropic(request,id):
        if request.method == "POST":
            a = CustomUser.objects.get(pk=id)
            form = CustomUserProfileForm(request.POST, request.FILES,instance=a)
            if form.is_valid(): 
                form.save()
            return redirect("doctorMyProfile")
        







@login_required(login_url='UserLogin') 
def doctorMarkCompeleted(request,id ):
       change = BookingPatient.objects.get(id=id)
       change.state = "COMPLETED"   # change field
       change.save() # this will update only

       return redirect("myAppointmentDoctor")


@login_required(login_url='UserLogin')
def doctorMarkPending(request,id ):
       change = BookingPatient.objects.get(id=id)
       change.state = "PENDING"   # change field
       change.save() # this will update only

       return redirect("myAppointmentDoctor")

@login_required(login_url='UserLogin')
def doctorMarkDeleted(request,id ):
       change = BookingPatient.objects.get(id=id)
       change.state = "DELETED"   # change field
       change.save() # this will update only
       change.documents.delete()

       return redirect("myAppointmentDoctor")

       
@login_required(login_url='UserLogin')
def doctordocumentDelete(request,id ):
       change = BookingPatient.objects.get(id=id)
       change.documents.delete()   # change field
       # change.save() # this will update only

       return redirect("myAppointmentDoctor")







#backup


# def myAppointmentDoctor(request):
#        #getting Doctor ID
#        doctorId = Doctor.objects.values_list('id', flat=True).get(userID_id=request.user.id)
#        #getting all listid with doctor id
#        listId =  list(List.objects.filter(doctor_id=doctorId).values('id','department_id','hospital_id','timeslot_id'))
#        #getting booking list with same list id
#        AllBookingList=[]
#        for i in listId:
#               item = BookingPatient.objects.filter(lists_id=i['id'])
#               if(item.exists()): 
#                      #getting all booking patient with same list id
#                      bookinglist =list(item.values('id','state','appointmentDate','patient_id','lists_id').order_by('appointmentDate'))
#                      AllBookingList.append(bookinglist)


#        eachBookingList=[]
#        for i in AllBookingList:
#          for j in i:  
#               patientUserId=Patient.objects.values_list('userID_id', flat=True).get(id=j['patient_id'])
#               hospitalId=List.objects.values_list('hospital_id', flat=True).get(id=j['lists_id'])
#               departmentId=List.objects.values_list('department_id', flat=True).get(id=j['lists_id'])
#               timeslotId=List.objects.values_list('timeslot_id', flat=True).get(id=j['lists_id'])

#               item ={'patientName':CustomUser.objects.values_list('first_name', flat=True).get(id=patientUserId),
#                      'patientstate':j['state'],
#                      'appointmentDate':str(j['appointmentDate']),
#                      'hospitalName':Hospital.objects.values_list('name', flat=True).get(id=hospitalId),
#                      'depName':Department.objects.values_list('name', flat=True).get(id=departmentId),
#                      'timeslot':Timing.objects.values_list('timeslot', flat=True).get(id=timeslotId),
#                      'bkTableToken':j['id'],
#                             }
#               eachBookingList.append(item) 

#        # if request.method == "POST":
#        #        instance = BookingPatient.objects.get(patient_id=1,lists_id=4,appointmentDate='2022-10-19',state='COMPLETED')
#        #        form = BookingPatientForm(request.POST, request.FILES, instance=instance)
#        #        if form.is_valid():
#        #               form.save()
#        #               return redirect("myAppointmentDoctor")

#        # form = BookingPatientForm()

#        context={'doctorId':doctorId , 'eachBookingList':json.dumps(eachBookingList)}

#        return render(request, "doctorApp/myAppointments.html",context)

#  #just for creating url
# def  docCreateUrlMarkCompeleted(request):
#        pass
# def  docCreateUrlMarkPending(request):
#        pass
# def  docCreateUrlMarkDeleted(request):
#        pass
 




# def doctorMarkCompeleted(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "COMPLETED"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")

# def doctorMarkPending(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "PENDING"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")

# def doctorMarkDeleted(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "DELETED"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")
   


#bc1

#    def homeDoctor(request):

#        return render(request, "doctorApp/home.html")

# def myAppointmentDoctor(request):
#        #getting Doctor ID
#        doctorId = Doctor.objects.values_list('id', flat=True).get(userID_id=request.user.id)
#        #getting all listid with doctor id
#        listId =  list(List.objects.filter(doctor_id=doctorId).values('id','department_id','hospital_id','timeslot_id'))
#        #getting booking list with same list id
#        AllBookingList=[]
#        for i in listId:
#               item = BookingPatient.objects.filter(lists_id=i['id'])
#               if(item.exists()): 
#                      #getting all booking patient with same list id
#                      bookinglist =list(item.values('id','state','appointmentDate','patient_id','lists_id').order_by('appointmentDate'))
#                      AllBookingList.append(bookinglist)

#        print(AllBookingList)
#        eachBookingList=[]
#        for i in AllBookingList:
#          for j in i:  
#               patientUserId=Patient.objects.values_list('userID_id', flat=True).get(id=j['patient_id'])
#               hospitalId=List.objects.values_list('hospital_id', flat=True).get(id=j['lists_id'])
#               departmentId=List.objects.values_list('department_id', flat=True).get(id=j['lists_id'])
#               timeslotId=List.objects.values_list('timeslot_id', flat=True).get(id=j['lists_id'])

#               item ={'patientName':CustomUser.objects.values_list('first_name', flat=True).get(id=patientUserId),
#                      'patientstate':j['state'],
#                      'appointmentDate':str(j['appointmentDate']),
#                      'hospitalName':Hospital.objects.values_list('name', flat=True).get(id=hospitalId),
#                      'depName':Department.objects.values_list('name', flat=True).get(id=departmentId),
#                      'timeslot':Timing.objects.values_list('timeslot', flat=True).get(id=timeslotId),
#                      'bkTableToken':j['id'],
#                             }
#               eachBookingList.append(item) 
       
#        # print(eachBookingList)


#        context={'doctorId':doctorId , 'eachBookingList':eachBookingList}

#        return render(request, "doctorApp/myAppointments.html",context)

#  #just for creating url
# def  docCreateUrlMarkCompeleted(request):
#        pass
# def  docCreateUrlMarkPending(request):
#        pass
# def  docCreateUrlMarkDeleted(request):
#        pass
 




# def doctorMarkCompeleted(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "COMPLETED"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")

# def doctorMarkPending(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "PENDING"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")

# def doctorMarkDeleted(request,id ):
#        change = BookingPatient.objects.get(id=id)
#        change.state = "DELETED"   # change field
#        change.save() # this will update only

#        return redirect("myAppointmentDoctor")





