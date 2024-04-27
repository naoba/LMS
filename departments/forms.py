from django.forms import ModelForm
from .models import Department, Subdepartment

class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = "__all__"

class SubdepartmentForm(ModelForm):

    class Meta:
        model = Subdepartment
        fields = "__all__"