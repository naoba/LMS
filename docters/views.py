from django.shortcuts import render, HttpResponse, redirect
from .models import RefDoctor
from .forms import RefDoctorForm

# Create your views here.

def RefLists(request):
    
    refdoctors= RefDoctor.objects.all()

    context={ "refdoctors": refdoctors}

    return render(request,'doctors/reflists.html', context)
    # return HttpResponse(" <h1> RefList View </h1>")

def RefCreate(request):

    if request.method == "POST":
        form = RefDoctorForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            refchk=RefDoctor.objects.filter(refname=item.refname).count()
            if refchk >= 1:
                return render(request, 'doctors/refcreate.html', {'form': form, })
            
            item.save()
            return redirect('reflists', )
    else:
        form = RefDoctorForm()
    return render(request, 'doctors/refcreate.html', {'form': form, })