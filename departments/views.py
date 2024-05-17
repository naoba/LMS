from django.shortcuts import render

from departments.models import Department, Subdepartment


# Create your views here.


def DepartmentLists(request):

    depts = Department.objects.all()
    subdepts = Subdepartment.objects.all()
    
    context = {'depts':depts, 'subdepts': subdepts }  
    return render(request, 'departments/departmentlist.html', context)


