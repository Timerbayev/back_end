from django.contrib import admin
from .models import Users


class AdminUser(admin.ModelAdmin):
    fields = ['username', 'password']
# Register your models here.


admin.site.register(Users, AdminUser)