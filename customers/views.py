from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.core.paginator import Paginator

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

