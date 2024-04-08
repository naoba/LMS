from django.contrib import admin

# Register your models here.

from .models import Designation, GStatus, Gender, RStatus

admin.site.register(Designation)
admin.site.register( GStatus)
admin.site.register(Gender)
admin.site.register(RStatus)
