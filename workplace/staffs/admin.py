from django.contrib import admin
from .models import Staffer


class Adminstaffs(admin.ModelAdmin):
    fields = ['first_name', 'last_name',  'slug', 'specialization', 'work_experience']


admin.site.register(Staffer, Adminstaffs)
