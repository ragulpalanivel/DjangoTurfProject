from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mainapp.models import Turf

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    TIME_SLOTS = [
        ('06:00-07:00 AM', '06:00-07:00 AM'),
        ('07:00-08:00 AM', '07:00-08:00 AM'),
        ('08:00-09:00 AM', '08:00-09:00 AM'),
        ('05:00-06:00 PM', '05:00-06:00 PM'),
        ('06:00-07:00 PM', '06:00-07:00 PM'),
        ('07:00-08:00 PM', '07:00-08:00 PM'),
        ('08:00-09:00 PM', '08:00-09:00 PM'),
        ('09:00-10:00 PM', '09:00-10:00 PM'),
        ('10:00-11:00 PM', '10:00-11:00 PM'),
        ('11:00-12:00 AM', '11:00-12:00 AM'),
        ('12:00-01:00 AM', '12:00-01:00 AM'),
        ('01:00-02:00 AM', '01:00-02:00 AM'),
    ]
    
    SPORT_CHOICES = [
        ('CRICKET', 'Cricket'),
        ('FOOTBALL', 'Football'),
        ('BADMINTON', 'Badminton'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    time_slot = models.CharField(max_length=30, choices=TIME_SLOTS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.turf.name} at {self.time_slot}"
