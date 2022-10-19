from django.db import models
from userSystem.models import CustomUser
import hospital.models
# Create your models here.

class Doctor(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    
    def __str__(self):
     return f' {self.userID}'


class DoctorList(models.Model):
    doctorName= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospitalName= models.ForeignKey("hospital.Hospital", on_delete=models.CASCADE)
    is_active=models.IntegerField(default=1)

    class Meta:
     unique_together = ( 'doctorName','hospitalName')

    def __str__(self):
     return f' {self.doctorName,self.hospitalName}'