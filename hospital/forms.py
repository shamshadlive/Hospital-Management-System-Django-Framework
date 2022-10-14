from django import forms
from .models import BookingPatient 
from crispy_forms.helper import FormHelper

# # # Create your forms here.
class BookingPatientForm(forms.ModelForm):

    class Meta:
        model = BookingPatient
        fields = ('documents',)
        labels = {'documents': ('Upload Prescription')}
 
       