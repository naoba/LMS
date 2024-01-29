from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer
from django.core.paginator import Paginator
from .forms import CustomerForm

# Create your views here.

def CustomerLists(request):
    customers_list = Customer.objects.all()
    paginator = Paginator(customers_list, 25)

    page_number = request.GET.get("page")
    customers = paginator.get_page(page_number)

    context = {'customers':customers}  
    return render(request, 'customers/customerlist.html', context)

def CustomerView(request, pk):

    customer = Customer.objects.get(id=pk)

    context = {'customer':customer}  
    return render(request, 'customers/customerview.html', context)

def CustomerCreate(request):

    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["file"])
            item = form.save(commit=False)
            item.save()
            return redirect('customerview', pk=item.pk)
    else:
        form = CustomerForm()
    return render(request, 'customers/customercreate.html', {'form': form, })


def CustomerEdit(request, pk):

    customer = get_object_or_404(Customer, id=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer,)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customerview', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customers/customercreate.html', {'form': form,'title':pk})

