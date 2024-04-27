from django.db import models
from general.models import GStatus

# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length=100)
    status =models.ForeignKey(GStatus,on_delete=models.SET_NULL,blank=True,null=True,)
    createat = models.DateTimeField(blank=True, auto_now_add=True)
    # createby = models.ForeignKey(blank=True)
    uodateat = models.DateTimeField(blank=True, auto_now=True)
    # updateby = models.ForeignKey(blank=True,)

    def __str__(self):
        return self.name

class Subdepartment(models.Model):

    name = models.CharField(max_length=100)
    department =models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True,)
    status =models.ForeignKey(GStatus,on_delete=models.SET_NULL,blank=True,null=True,)
    createat = models.DateTimeField(blank=True, auto_now_add=True)
    # createby = models.ForeignKey(blank=True)
    uodateat = models.DateTimeField(blank=True, auto_now=True)
    # updateby = models.ForeignKey(blank=True,)

    def __str__(self):
        return self.name

