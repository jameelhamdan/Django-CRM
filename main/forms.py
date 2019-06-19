from django import forms
from .models import *
from django.forms.models import *
from django.forms.models import inlineformset_factory

class CustomerForm(forms.ModelForm):
    #myservices = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,queryset = service.objects.all())
    #myservices = CServiceFormSet()
    class Meta:
        model = customer
        fields = ["name", "phonenumber"]


class CServiceForm(forms.ModelForm):
    class Meta:
        model = customerservice
        fields = ["active"]

    myservice = forms.ModelChoiceField(queryset = service.objects.all(),)



CServiceFormSet = inlineformset_factory(customer, customerservice, CServiceForm)

#service form
class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        exclude = ()