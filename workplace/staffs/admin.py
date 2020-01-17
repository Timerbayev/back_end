from django.contrib import admin
from .models import Staffer, Education


class Adminstaff(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'age', 'slug', 'occupation', 'specialization', 'education', 'work_experience',
              'img']


admin.site.register(Staffer, Adminstaff)


class Study(admin.ModelAdmin):
    fields = ['study', 'data', 'place']


admin.site.register(Education, Study)




