from django.contrib import admin

# Register your models here.
from .models import Department, Subdepartment


admin.site.register(Department)
admin.site.register(Subdepartment)