from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePatient(request):
       return render(request, "patientApp/home.html")


def loginPatient(request):
       return render(request, "patientApp/login.html")

def registerPatient(request):
       return render(request, "patientApp/register.html")


def resetPasswordPatient(request):
       return render(request, "patientApp/resetPassword.html")




#check username
def checkUsername(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        getdata=json.load(request) 
        id = getdata['id']
        user_name = getdata['usernameCheck']
        data = {
            'id': id,
            'is_taken': User.objects.filter(username=user_name).exists(),
             }
        return JsonResponse(data)
    else:
        return redirect('/')

#check username
def checkPhone(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        getdata=json.load(request) 
        id = getdata['id']
        phone_number = getdata['phoneCheck']
        data = {
            'id': id,
            'is_taken': User.objects.filter(phone_number=phone_number).exists(),
             }
        return JsonResponse(data)
    else:
        return redirect('/')


#check email whtther taken or not
def checkEmail(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
      if request.method == 'POST':
        getdata=json.load(request) 
        id = getdata['id']
        email_id = getdata['emailCheck']
        data = {
            'id': id,
            'is_taken': User.objects.filter(email=email_id).exists(),
             }
        return JsonResponse(data)
    else:
        return redirect('/')