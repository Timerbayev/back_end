from django.db import models


class Patients(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     birthday = models.DateField(blank=True)
     address = models.CharField(max_length=50)
     mobile = models.CharField(max_length=50, default="")
     email = models.EmailField(max_length=50, default="")
     social_status = models.CharField(max_length=50)
     complaint = models.TextField(max_length=200)
     history = models.TextField(max_length=200)

# Create your models here.
