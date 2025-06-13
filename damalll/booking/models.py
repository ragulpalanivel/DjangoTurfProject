from django.db import models
from django.contrib.auth.models import User 

from mainapp.models import Turf
# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    
