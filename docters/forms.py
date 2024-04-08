from django.forms import ModelForm, Textarea, CharField, ImageField, FileInput, IntegerField, DateField
from django.utils.translation import gettext_lazy as _
from .models import RefDoctor
from django import forms


class RefDoctorForm(ModelForm):

    
    class Meta:
        model = RefDoctor
        
        fields = "__all__"
        widgets = {
            'refdob':forms.DateInput(attrs={'value':'', }),
            'refdoa':forms.DateInput(attrs={'value':'', }),
            
        }
        labels = {
            "refname": _("Referal Name"),
            "display": _("Display Name"),
            "refmobile": _("Mobile"),
            "refphone": _("Phone"),
            "refemail": _("Email"),
            "refregister": _("Regn No."),
            "refspeciality": _("Speciality"),
            "refaddress": _("Full Adress"),
            "refstate": _("State"),
            "refcountry": _("Country"),
            "refpincode": _("Pin-Code"),
            "refdob": _("DOB"),
            "refdoa": _("DOA"),
            "refpricelist": _("Price List"),
            "refreport": _("Report"),
            

        }