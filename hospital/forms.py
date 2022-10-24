from django import forms
from .models import * 


# # # Create your forms here.
class BookingPatientForm(forms.ModelForm):

    class Meta:
        model = BookingPatient
        fields = ('documents',)
        labels = {'documents': ('Upload Prescription')}
 
class AddHospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ('name','hos_type','district')
        labels = {'name': ('Hospital Name'),
                  'hos_type': ('Type of Hospital'),
                  'district': ('District'),}

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ['hospital']