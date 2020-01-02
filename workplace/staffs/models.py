from django.db import models
from django.shortcuts import reverse


class Staffer (models.Model):
    object = models.Manager()
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    slug = models.SlugField(max_length=50, default='')
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    position = models.CharField(max_length=50, default='')
    specialization = models.CharField(max_length=50, default='')
    work_experience = models.IntegerField(default=0)
    scientific_degree = models.CharField(max_length=100)
    dismissed = models.BooleanField(default=False)
    img = models.ImageField(upload_to="static/bootstrap/img/", height_field=None, width_field=None, max_length=100)

    def get_absolute_url(self):
        return reverse('persons', kwargs={'slug': self.slug})
