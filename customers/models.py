from django.db import models

class Customer(models.Model):
    GENDER = {
        "M": "Male",
        "F": "Female",
        "O": "Other",}
    USERSS={
        '1': "Tom"
    }

    title = models.CharField(blank=True,max_length=10)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    mobile = models.IntegerField(blank=True,)
    phone = models.IntegerField(blank=True,)
    adress = models.CharField(blank=True,max_length=150)
    state = models.CharField(blank=True,max_length=50)
    country = models.CharField(blank=True,max_length=50)
    pincode = models.IntegerField(blank=True,max_length=10)
 #   doc_upload= models.CharField(blank=True,max_length=30)
 #   createat = models.DateField(blank=True,)
 #   createby = models.ForeignKey(blank=True,USERSS,)
 #   uodateat = models.DateField(blank=True,)
 #   updateby = models.ForeignKey(blank=True,USERSS,)
