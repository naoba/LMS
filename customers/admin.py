from django.contrib import admin

# Register your models here.
from .models import Customer, JEmodel

admin.site.register(Customer)
admin.site.register(JEmodel)