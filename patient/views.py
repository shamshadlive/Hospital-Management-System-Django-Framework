from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login ,logout ,get_user_model
from django.contrib.auth.decorators import login_required
from userSystem.models import User,CustomUser
from .models import Patient
from hospital.models import *
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
import json
import datetime
# Create your views here.

User = get_user_model()



# @login_required(login_url='UserLogin')
def homePatient(request):
        userid=request.user.id
        patient = Patient.objects.get(userID=userid)
        context={'patient':patient,}
       
        return render(request, "patientApp/home.html",context)


#New Appointmetnt Patient
#Redirect unauthorized user's from accessing home page
@login_required(login_url='login')
@never_cache
def patientNewbooking(request):
       
    userid=request.user.id
    #getting basic patient details
    patient = Patient.objects.get(userID_id=userid)

    #hospital = serializers.serialize("json", Hospital.objects.all())
    #gethospital
    hospital =   json.dumps( list(Hospital.objects.values('name','district','hos_type','id')) ) 

    context={'patient':patient , 'hospital':hospital, }
    return render(request, 'patientApp/newBooking.html',context)


#choose doctor for Patient
#Redirect unauthorized user's from accessing home page
@login_required(login_url='login')
@never_cache
def patientChooseDoctor(request):

    userid=request.user.id
    #getting basic patient details
    patient = Patient.objects.get(userID_id=userid)

    if request.method == 'POST':


        #getting form submitted values
        selectedHosDistrict = request.POST['hospital_district']
        selectedHosType = request.POST['hospital_type']
        selectedHosName = request.POST['hospital_name']
        selectedHosDepartment = request.POST['hospital_department']

        #get hospital id
        hospitalId =  Hospital.objects.values_list('id', flat=True).get(name=selectedHosName)
       
        #get doctor and time slot of doctor
        doctorDetailsID = List.objects.filter(hospital_id=hospitalId).values('doctor_id','timeslot_id','department_id') 

        doctorDetails=[]
        for i in doctorDetailsID:
            #doctor user id
            doctorUserId=Doctor.objects.values_list('userID_id', flat=True).get(id=i['doctor_id']) 
            #getting doctor name and timeslot
            doc ={'doctorName':CustomUser.objects.values_list('first_name', flat=True).get(id=doctorUserId), 'doctorSlot':Timing.objects.values_list('timeslot', flat=True).get(id=i['timeslot_id']),
            'doctorDep':Department.objects.values_list('name', flat=True).get(id=i['department_id'])}

            # doc ={'doctorName':Doctor.objects.values_list('name', flat=True).get(id=i['doctor_id']) , 'doctorSlot':Timing.objects.values_list('timeslot', flat=True).get(id=i['timeslot_id']),
            # 'doctorDep':Department.objects.values_list('name', flat=True).get(id=i['department_id'])}
            doctorDetails.append(doc)
       
        context={
            'patient':patient, 
            'selectedHosDistrict':selectedHosDistrict , 
            'selectedHosType':selectedHosType, 
            'selectedHosName':selectedHosName,
            'selectedHosDepartment':selectedHosDepartment,
            'doctorDetails':json.dumps(doctorDetails)}
        return render(request, 'patientApp\chooseDoctor.html',context)

#choose doctor for Patient
#Redirect unauthorized user's from accessing home page
@login_required(login_url='login')
def patientSaveBooking(request,dep ,hosname ,uhid):

    if request.method == 'POST':


        #getting data
        selectedDoctor = request.POST['doctor_name']
        selectedTimeslot = request.POST['doctor_timeSlot']
        selectedAppointDate = request.POST['AppointDate']
        selectedHospital = hosname

        #getting all ids
        docId=Doctor.objects.values_list('id', flat=True).get(name=selectedDoctor)
        depId=Department.objects.values_list('id', flat=True).get(name=dep)
        timeSlotId=Timing.objects.values_list('id', flat=True).get(timeslot=selectedTimeslot)
        hosId=Hospital.objects.values_list('id', flat=True).get(name=hosname)

        #getting id of list
        listsid=List.objects.values_list('id', flat=True).get(department_id=depId,doctor_id=docId,hospital_id=hosId,timeslot_id=timeSlotId)
        patientid=Patient.objects.values_list('id', flat=True).get(patient_uhid=uhid)

        userid=request.user.id
        #getting basic patient details
        patient = Patient.objects.get(userID_id=userid)
        context={
                'patient':patient}


        if(BookingPatient.objects.filter(appointmentDate=selectedAppointDate,patient_id=patientid,lists_id=listsid).exists()):

            messages.error(request, 'You have already booked with same details , please check the My booking page')   
            return render(request, 'patientSystem_Templates\patient_BookingSucess.html',context)



        else:

            bookingpatient=BookingPatient.objects.create(state='PENDING',patient_id=patientid,lists_id=listsid ,appointmentDate=selectedAppointDate )
            bookingpatient.save()

           
            messages.success(request, 'Your boooking successfully completed')  
            return render(request, 'patientSystem_Templates\patient_BookingSucess.html',context)




#get Deparment
def getHospitalDepartment(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        #loading all data
        getdata=json.load(request) 
        #getting hospital id
        gethospital_id = getdata['hospital_id']
        #geting all ids from list 
        getdepartment_ids =  List.objects.filter(hospital_id=gethospital_id).values('department_id')
        
        getdepartmentValue=[]

        #appending values from department table

        for i in getdepartment_ids:
            getdepartmentValue.append( list(Department.objects.filter(id=i['department_id']).values('name')) )
       
     
    
        data={
            'getdepartmentValue':getdepartmentValue
        }
     
        return JsonResponse(data)
    else:
        return redirect('patient-home')


#Patient Profile Booking
#Redirect unauthorized user's from accessing home page
@login_required(login_url='login')
def patientViewBooking(request):

    userid=request.user.id
    #getting basic patient details
    patient = Patient.objects.get(userID_id=userid)

    #getting patient ID
    patientId = Patient.objects.values_list('id', flat=True).get(userID_id=userid)

    #getting booking list of that patient
    bookingList = list(BookingPatient.objects.filter(patient_id=patientId).values('lists_id','state','appointmentDate').order_by('appointmentDate') )

    #getting all ids
    eachListID=[]
    for i in bookingList:
            eachListIDs ={'doctor_id':List.objects.values_list('doctor_id', flat=True).get(id=i['lists_id']),
                        'timeslot_id':List.objects.values_list('timeslot_id', flat=True).get(id=i['lists_id']),
                        'department_id':List.objects.values_list('department_id', flat=True).get(id=i['lists_id']),
                        'hospital_id':List.objects.values_list('hospital_id', flat=True).get(id=i['lists_id']),
                        'state':i['state'],
                        'appointmentDate':str(i['appointmentDate'])
                         }
            eachListID.append(eachListIDs)   
          
    finalBookingList=[]
    #getting all values
    for j in eachListID:
             eachListName ={'doctorName':Doctor.objects.values_list('name', flat=True).get(id=j['doctor_id']) ,
                        'doctorSlot':Timing.objects.values_list('timeslot', flat=True).get(id=j['timeslot_id']),
                        'doctorDep':Department.objects.values_list('name', flat=True).get(id=j['department_id']),
                        'hospital':Hospital.objects.values_list('name', flat=True).get(id=j['hospital_id']),
                        'state':j['state'],
                        'appointmentDate':str(j['appointmentDate'])
                        }
             finalBookingList.append(eachListName)

    context={
            'patient':patient,'bookinglist':json.dumps(finalBookingList)}

    return render(request, 'patientSystem_Templates\patient_ViewBooking.html',context)

#Patient Profile 
#Redirect unauthorized user's from accessing 
@login_required(login_url='login')
def patientMyProfile(request):

    userid=request.user.id
    #getting basic patient details
    patient = Patient.objects.get(userID_id=userid)
    context={
                'patient':patient}

    return render(request, 'patientSystem_Templates\patient_MyProfile.html',context)

