from django.db import models


class Department(models.Model):
    specialization = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number_staff = models.IntegerField(default=0)

    def __str__(self):
        return self.specialization

    class Meta:
        ordering = ['specialization']

# Create your models here.
