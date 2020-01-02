from django.contrib import admin
from .models import Users


class AdminUsers(admin.ModelAdmin):
    fields = ['username', 'password']
# Register your models here.


admin.site.register(Users, AdminUsers)