from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def CustomerLists(request):

    #return HttpResponse('<h1>Hello HttpResponse</h1>')
    return render(request, 'base.html')
