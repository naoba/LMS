from django.shortcuts import render

from departments.models import Department, Subdepartment


# Create your views here.


def DepartmentLists(request):

    dept = Department.objects.all()
    context = {'customers':dept}  
    return render(request, 'customers/customerlist.html', context)

def SubdepartmentLists(request):

    dept = Subdepartment.objects.all()
    context = {'customers':dept}  
    return render(request, 'customers/customerlist.html', context)
