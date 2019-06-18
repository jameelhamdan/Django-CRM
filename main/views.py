from django.http import HttpResponse, Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import customer, service

def index(request):
    latest_customer = customer.objects.order_by('-name')[:5]
    context = {'latest_customer': latest_customer,}      
    return render(request, 'main/index.html', context)

def customers(request, customer_id=None):
    if customer_id is None :
        latest_customer = customer.objects.order_by('-name')
        context = {'latest_customer': latest_customer}      
        return render(request, 'main/customers.html', context)
    else :
        try:
            cc = customer.objects.get(pk=customer_id)
        except:
            raise Http404("Customer does not exist")
        return render(request, 'main/customer.html', {'customer': cc})


def customersadd(request):
    #gettings formdata
    try:
        cc = customer(phonenumber=request.POST['phonenumber'],name = request.POST['name'])
        cc.save()

        return redirect('main:customers')        
    except:
        return redirect('main:customers')

def customersdelete(request,customer_id):
    try:
        cc = customer.objects.get(pk=customer_id)
        cc.delete()

        return redirect('main:customers')        
    except:
        return redirect('main:customers')
    

def services(request, service_id=None):
    if service_id is None :
        latest_service = service.objects.order_by('-name')
        context = {'latest_service': latest_service,}      
        return render(request, 'main/services.html', context)

    else :
        try:
            cc = service.objects.get(pk=service_id)
        except:
            raise Http404("Service does not exist")
        return render(request, 'main/service.html', {'service': cc})

def servicesadd(request):
    #gettings formdata
    try:
        cc = service(name = request.POST['name'])
        cc.save()

        return redirect('main:services')        
    except:
        return redirect('main:services')

def servicesdelete(request,service_id):
    try:
        cc = service.objects.get(pk=service_id)
        cc.delete()

        return redirect('main:services')        
    except:
        return redirect('main:services')