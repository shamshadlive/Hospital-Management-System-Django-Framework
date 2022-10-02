from django.db import models
from userSystem.models import CustomUser
# Create your models here.

class Doctor(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    
    def __str__(self):
     return f' {self.userID}'