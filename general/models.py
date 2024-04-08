from django.db import models

# Create your models here.

class Designation(models.Model):

    designation = models.CharField(max_length=10)

    def __str__(self):
        return self.designation
    
class GStatus(models.Model):

    gstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.gstatus
    
class RStatus(models.Model):

    rstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.rstatus
    
class Gender(models.Model):

    gender = models.CharField(max_length=5)

    def __str__(self):
        return self.gender

