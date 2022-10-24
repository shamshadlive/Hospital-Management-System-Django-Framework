from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital.models import Hospital,HospitalAdmin,Doctor
from doctor.models import *
from .models import *
import json
from django.http import JsonResponse
from .forms import AddHospitalForm,AddDoctorForm
from django.contrib.auth.decorators import login_required
from userSystem.forms import CustomUserProfileForm
from django.db import IntegrityError

# Create your views here.

def homeHospital(request):

       hosAdminData = list(HospitalAdmin.objects.filter(userID_id=request.user.id).values('id','is_active'))  
       for i in hosAdminData:
              if(i['is_active']):
                     #getting valid hospital admin id
                     hosAdminId=i['id']
       
       hospitalData = list(Hospital.objects.filter(createdBy=hosAdminId).values('id','name','hos_type','district','status'))  

       context={'hospitalData':hospitalData}

       return render(request, "hospitalApp/home.html",context)


#add new hospital
def addHospital(request): 
    if request.method == "POST":
       form = AddHospitalForm(request.POST)
       createdID=HospitalAdmin.objects.values_list('id', flat=True).get(userID_id=request.user.id)
       if form.is_valid():
              obj = form.save(commit=False)
              obj.createdBy_id = createdID
              obj.save()
              return redirect("homeHospital")
       else:  
              context={'form':form}
              return render(request, 'hospitalApp/addHospital.html',context)
    else:
       #Add new hospital
       form = AddHospitalForm()
       context={'form':form}
       return render(request, 'hospitalApp/addHospital.html',context)

#add new doctor
def addDoctor(request,id): 
    if request.method == "POST":
       form = AddDoctorForm(request.POST)

       if form.is_valid():
        try: 
              doctorID = form['doctor'].value()
              obj = form.save(commit=False)
              obj.hospital_id = id
              obj.save() 
        except IntegrityError as e:
              context={'form':form , 'excerror':"Same combination already added"}
              return render(request, 'hospitalApp/addDoctor.html',context)
        try:
              #saving to doctor list table
              DoctorList.objects.create(doctorName_id=doctorID,hospitalName_id=id)
              return redirect("homeHospital")
        except IntegrityError as e:
              return redirect("homeHospital")
       else:  
              context={'form':form}
              return render(request, 'hospitalApp/addDoctor.html',context)
    else:
       #Add new doctor
       form = AddDoctorForm()
       context={'form':form}
       return render(request, 'hospitalApp/addDoctor.html',context)




#delete hospital
@login_required(login_url='UserLogin')
def hospitalDelete(request,id ):
       Hospital.objects.get(id=id).delete()
       return redirect("homeHospital")



#view hospital details
@login_required(login_url='UserLogin')
def hospitalview(request,getname ):
       hospitalData=Hospital.objects.filter(name=getname).values('name','hos_type','id')
       #getting hospital id
       hospitalid=0
       for i in hospitalData:
              hospitalid=i['id']

       hospitalID=hospitalid
       #getting doctor id
       doctorID=DoctorList.objects.filter(hospitalName_id=hospitalID).values('id','doctorName_id','is_active')
       doctorData=[]
       #to get active doctor count
       activedoctorNo=0
       for i in doctorID:
              eachUserID= Doctor.objects.values_list('userID_id', flat=True).get(id=i['doctorName_id'])
              doctorName=CustomUser.objects.values_list('first_name', flat=True).get(id=eachUserID)
              doctorData.append({'doctorName':doctorName,'is_active':i['is_active'],'doctorlistToken':i['id']})
              if(i['is_active']):
                     activedoctorNo=activedoctorNo+1

       listIDs=List.objects.filter(hospital_id=hospitalID).values('id')
       COMPLETEDVS=0
       DELETEDVS=0
       PENDINGVS=0
       #getting count directly from the db
       for i in listIDs:
              COMPLETED=BookingPatient.objects.filter(lists_id=i['id']).filter(state='COMPLETED').count()
              COMPLETEDVS=COMPLETED+COMPLETEDVS

              DELETED=BookingPatient.objects.filter(lists_id=i['id']).filter(state='DELETED').count()
              DELETEDVS=DELETED+DELETEDVS

              PENDING=BookingPatient.objects.filter(lists_id=i['id']).filter(state='PENDING').count()
              PENDINGVS=PENDING+PENDINGVS
   
       context={'hospitalData':hospitalData,'doctorData':doctorData,'activedoctorNo':activedoctorNo,'COMPLETEDVS':COMPLETEDVS,'DELETEDVS':DELETEDVS,'PENDINGVS':PENDINGVS}
       return render(request, 'hospitalApp/hospitalDetails.html',context)



#Doctor Profile 
#Redirect unauthorized user's from accessing 
@login_required(login_url='UserLogin')
def hosadminMyProfile(request):


    #profile pic
    formset = CustomUserProfileForm()
    context={'formset':formset,}

    return render(request, 'hospitalApp/profile.html',context)

#user pro pic
def uploadHosAdminPropic(request,id):
        if request.method == "POST":
            a = CustomUser.objects.get(pk=id)
            form = CustomUserProfileForm(request.POST, request.FILES,instance=a)
            if form.is_valid(): 
                form.save()
            return redirect("hosadminMyProfile")
        





#changeStatus Hospital
def changeStatusHospital(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        getdata=json.load(request) 
        id = getdata['id']
        status = getdata['status']
        hospital = Hospital.objects.get(id=id)
        hospital.status = status
        hospital.save()      
        data = {
            'status': True,
               }
        return JsonResponse(data)
      else:
        data = {
            'status': False,
               }
        return JsonResponse(data)
    else:
        return redirect('/')

#changeStatusHospitalDoctor Hospital
def changeStatusHospitalDoctor(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        getdata=json.load(request) 
        id = getdata['id']
        status = getdata['status']
        doctorlist = DoctorList.objects.get(id=id)
        doctorlist.is_active = status
        doctorlist.save()      
        data = {
            'status': True,
               }
        return JsonResponse(data)
      else:
        data = {
            'status': False,
               }
        return JsonResponse(data)
    else:
        return HttpResponse("Homepage")