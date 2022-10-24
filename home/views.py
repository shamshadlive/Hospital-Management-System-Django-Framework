from django.shortcuts import render
from django.http import HttpResponse









def home(request):

       return render(request, 'homeApp/home.html')
def about(request):

       return render(request, 'homeApp/aboutus.html')

def contact(request):

       return render(request, 'homeApp/contact.html')
