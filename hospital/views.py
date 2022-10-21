from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital.models import Hospital,HospitalAdmin
from doctor.models import *
import json
from django.http import JsonResponse
from .forms import AddHospitalForm
from django.contrib.auth.decorators import login_required
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
       hospitalID=Hospital.objects.values_list('id', flat=True).get(name=getname)
       #getting doctor id

       doctorID=DoctorList.objects.filter(hospitalName_id=hospitalID).values('id','doctorName_id','is_active')
       doctorData=[]
       activedoctorNo=0
       for i in doctorID:
              eachUserID= Doctor.objects.values_list('userID_id', flat=True).get(id=i['doctorName_id'])
              doctorName=CustomUser.objects.values_list('first_name', flat=True).get(id=eachUserID)
              doctorData.append({'doctorName':doctorName,'is_active':i['is_active'],'doctorlistToken':i['id']})
              context={'hospitalData':hospitalData,'doctorData':doctorData}
              return render(request, 'hospitalApp/hospitalDetails.html',context)

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