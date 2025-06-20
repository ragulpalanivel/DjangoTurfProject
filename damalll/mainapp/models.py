from django.db import models

class Turf(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to= 'media/turf/', null=True)

    def __str__(self):
        return self.name