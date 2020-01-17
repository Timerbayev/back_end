from django.db import models
from django.shortcuts import reverse


class Education(models.Model):
    study = models.CharField(max_length=100, default='')
    data = models.DateField()
    place = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.study


class Staffer(models.Model):
    object = models.Manager()
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, default='')
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    position = models.CharField(max_length=50, default='')
    occupation = models.CharField(max_length=50, default='')
    specialization = models.CharField(max_length=50, default='')
    work_experience = models.IntegerField(default=0)
    education = models.ForeignKey(Education, null=True, on_delete=models.SET_NULL)
    scientific_degree = models.CharField(max_length=100, default='')
    dismissed = models.BooleanField(default=False)
    img = models.ImageField(upload_to="media/images/",  height_field=None, width_field=None, max_length=100)

    def get_absolute_url(self):
        return reverse('persons', kwargs={'slug': self.slug})

    def __str__(self):
        return self.last_name






