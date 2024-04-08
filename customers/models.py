from django.db import models
from django.utils import timezone
from datetime import datetime
from general.models import Gender, Designation

class Customer(models.Model):
    GENDER = {
        "M": "Male",
        "F": "Female",
        "O": "Other",}
    USERSS={
        '1': "Tom"
    }
    ## NOTE null = True : Emtry database, blank = True : Emtry from
    ## auto_now_add: one time when first create, auto_now: every time to save

    title =models.ForeignKey(Designation,on_delete=models.SET_NULL,blank=True,null=True,)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.ForeignKey(Gender,on_delete=models.SET_NULL,blank=True,null=True,)
    mobile = models.IntegerField(null = True, blank=True,)
    phone = models.IntegerField(blank=True, null = True)
    email = models.EmailField(blank=True, null = True)
    adress = models.CharField(blank=True,max_length=150)
    state = models.CharField(blank=True,max_length=50, null = True)
    country = models.CharField(blank=True,max_length=50, null = True)
    pincode = models.IntegerField(blank=True,max_length=10, null = True)
    photo= models.ImageField(blank=True,upload_to="static/uploads/customers", null = True)
    doc_upload= models.FileField(blank=True,upload_to="static/uploads/doc", null = True)
    createat = models.DateTimeField(blank=True, auto_now_add=True)
    # createby = models.ForeignKey(blank=True)
    uodateat = models.DateTimeField(blank=True, auto_now=True)
    # updateby = models.ForeignKey(blank=True,)

    def __str__(self):
        return self.title+' '+self.full_name
    
    def get_absolute_url(self):
        return f"/customer/{self.id}/"
 
    @property
    def age(self):
    # Get the current date
        current_date = timezone.now().date()
    
    # Calculate the age
        age = current_date - self.dob
    
    # Extract years, months, and days from the age
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
    
        return f"{years}y {months}m {days}d"
    
    @property
    def customer_days(self):
        current_date = timezone.now().date()
        age = current_date - self.dob
    
        return age.days
    
    

