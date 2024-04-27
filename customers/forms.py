# myapp/forms.py
from django.forms import ModelForm, Textarea, CharField, ImageField, FileInput, IntegerField, DateField
from django.utils.translation import gettext_lazy as _
from .models import Customer, JEmodel
from django import forms
from django.utils import timezone

class CustomerForm(ModelForm):

    
    class Meta:
        model = Customer
        # fields = ['title','full_name', 'dob', 'gender', 'mobile', 'phone', 'email', 'adress', 'state', 'country', 'pincode', 'photo', 'doc_upload']
        fields = "__all__"
        widgets = {
            # 'dob': DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}), input_formats=('%d/%m/%Y', ))
            'dob':forms.DateInput(attrs={'value':timezone.now().date(), 'onchange': "DOBtoAge()"}),
            
        }
        labels = {
            "title": _("Title"),
            "full_name": _("Full Name"),
            "dob": _("Date of Birth"),
            "age": _("Age"),
            "gender": _("Gender"),
            "mobile": _("Mobile No"),
            "phone": _("Alt Phone No"),
            "email": _("Email Adress"),
            "adress": _("Adress"),
            "state": _("State"),
            "pincode": _("Pin-Code"),
            "country": _("Country"),
            "photo": _("Photo"),
            "doc_upload": _("Doc Upload"),

        }


class JEForm(ModelForm):
    class Meta:
        model= JEmodel
        fields = "__all__"
        
    
        

   
