from django.shortcuts import render
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
        form = CustomerForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = CustomerForm()
    return render(request, 'customers/customercreate.html', {'form': form})

