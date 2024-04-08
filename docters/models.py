from django.db import models

# Create your models here.


class RefDoctor(models.Model):

    refname = models.CharField(max_length=150)
    display = models.CharField(max_length=150)
    refmobile = models.IntegerField(null=True, blank=True,max_length=10)
    refphone = models.IntegerField(null=True, blank=True,max_length=10)
    refemail = models.EmailField(null=True, blank=True,max_length=10)
    refregister = models.CharField(null=True, blank=True,max_length=10)
    refspeciality = models.CharField(null=True, blank=True,max_length=10)
    refaddress = models.CharField(null=True, blank=True,max_length=250)
    refstate = models.CharField(null=True, blank=True,max_length=100)
    refcountry = models.CharField(null=True, blank=True,max_length=100)
    refpincode = models.IntegerField(null=True, blank=True,max_length=10)
    refdob = models.DateField(null=True, blank=True,)
    refdoa = models.DateField(null=True, blank=True,)
    refpricelist = models.CharField(max_length=10,null=True, blank=True)
    refreport = models.BooleanField(default=False)
    refcreateat = models.DateTimeField(blank=True, auto_now_add=True)
    # createby = models.ForeignKey(blank=True)
    refupdateat = models.DateTimeField(blank=True, auto_now=True)
    # updateby = models.ForeignKey(blank=True,)

    def __str__(self):
        return 'Dr. '+self.display
