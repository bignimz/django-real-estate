from ctypes import addressof
from email.policy import default
from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title