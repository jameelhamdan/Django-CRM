from django.http import HttpResponse, Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.forms import inlineformset_factory

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
            srv = customerservice.objects.filter(customer=cc)
        except:
            raise Http404("Customer does not exist")
        return render(request, 'main/customer.html', {'customer': cc,"services":srv})


def customeradd(request):
    try:
        form = CustomerForm(request.POST)
        if form.is_valid():
            cc = customer()
            cc.name = form.cleaned_data['name']
            cc.phonenumber = form.cleaned_data['phonenumber']
            # for f in form.cleaned_data['myservices']:
            #     cs = customerservice()
            #     cs.customer = cc
            #     cs.service = f
            #     cs.save()                                
            cc.save()
            
        return HttpResponseRedirect(reverse('main:customeredit/' + customer.pk))
    except:
        return HttpResponseRedirect(reverse('main:customers'))
        

def customeredit(request,pk):
    cc = get_object_or_404(customer, pk=pk)
    FormSet = inlineformset_factory(customer, customerservice, form=CServiceForm,extra=1)

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        formset = FormSet(request.POST, instance=cc)

        if form.is_valid():
            cc.name = form.cleaned_data['name']
            cc.phonenumber = form.cleaned_data['phonenumber']
            #services here
            
            if formset.is_valid():
                formset.save()

            cc.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('main:customers'))

    formset = FormSet(instance=cc,)
    context = {
        "formset": formset,
        'form': CustomerForm(initial={'name': cc.name, 'phonenumber':cc.phonenumber }),
        'instance': cc,
    }

    return render(request, 'main/customeredit.html', context)

def customersdelete(request,customer_id):
    try:
        cc = customer.objects.get(pk=customer_id)
        cc.delete()
        return redirect('main:customers')        
    except:
        return redirect('main:customers')



#=============================================================#
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
    try:
        form = ServiceForm(request.POST)
        if form.is_valid():
            ss = service()
            ss.name = form.cleaned_data['name']                               
            ss.save()
            
        return HttpResponseRedirect(reverse('main:services'))
    except:
        return HttpResponseRedirect(reverse('main:services'))

def servicesdelete(request,service_id):
    try:
        cc = service.objects.get(pk=service_id)
        cc.delete()

        return redirect('main:services')        
    except:
        return redirect('main:services')
