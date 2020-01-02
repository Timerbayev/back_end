from django.contrib import admin
from .models import Department


class AdminDepartment(admin.ModelAdmin):
    fields = ['specialization', 'email']


admin.site.register(Department, AdminDepartment)
# Register your models here.
