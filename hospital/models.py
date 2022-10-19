from django.db import models
from userSystem.models import CustomUser
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.

class HospitalAdmin(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    
    def __str__(self):
     return f' {self.userID}'

class Hospital(models.Model):
    
    hos_Choices = (
            ('Taluk Headquarters Hospital', 'Taluk Headquarters Hospital'),
            ('Medical College Hospital', 'Medical College Hospital'),
            ('Family Health Center', 'Family Health Center'),
         
        )
    dct_Choices = (
        ('Alappuzha', 'Alappuzha'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'hiruvananthapuram'),
        ('Thrissur', 'Thrissur'),
        ('Wayanad', 'Wayanad'),
      
    )

    name = models.CharField(max_length=100,unique=True)
    hos_type = models.CharField(max_length=100,choices=hos_Choices)
    district = models.CharField(max_length=100,null=False, choices=dct_Choices)
    createdBy =models.ForeignKey(HospitalAdmin, on_delete=models.CASCADE)
    createdOn =models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(default=1)
 

    def __str__(self):
     return f'{self.name} {self.district}'


#Department list
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
     return f'{self.name}'



#Timing
class Timing(models.Model):

    Time_Choices = (
            ('7:00 AM - 9:00 AM', '7:00 AM - 9:00 AM'),
            ('10:00 AM - 12:00 PM', '10:00 AM - 12:00 PM'),
            ('1:00 PM - 3:00 PM', '1:00 PM - 3:00 PM'),
            ('4:00 PM - 6:00 PM', '4:00 PM - 6:00 PM'),
            ('NULL', 'Not Available'),
               
        )
    timeslot = models.CharField(max_length=100,choices=Time_Choices)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.timeslot}'



class List(models.Model):
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    timeslot=models.ForeignKey(Timing, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
     unique_together = ( 'hospital','doctor','department','timeslot')
    
    def __str__(self):
     return f'{self.doctor} {self.hospital} {self.department} {self.timeslot}'


class BookingPatient(models.Model):
    state_Choices = (
            ('COMPLETED', 'COMPLETED'),
            ('PENDING', 'PENDING'),
            ('DELETED', 'DELETED'),           
        )

    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    state=models.CharField(max_length=20,choices=state_Choices , null=True , blank=True)
    lists=models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    appointmentDate=models.DateField()
    documents = models.FileField(upload_to='hospital/prescription',null=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.documents.name))
        super(Document,self).delete(*args,**kwargs)

    

    def __str__(self):
     return f'{self.patient}'
