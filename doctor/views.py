from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homeDoctor(request):

       return render(request, "doctorApp/home.html")
