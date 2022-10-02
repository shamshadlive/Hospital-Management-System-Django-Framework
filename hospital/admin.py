from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Timing)
admin.site.register(List)
admin.site.register(BookingPatient)
admin.site.register(HospitalAdmin)