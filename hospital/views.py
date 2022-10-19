from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital.models import *
import json
from django.http import JsonResponse
from .forms import AddHospitalForm
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