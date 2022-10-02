from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeHospital(request):

       return render(request, "hospitalApp/home.html")

