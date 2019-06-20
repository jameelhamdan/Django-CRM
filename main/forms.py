from django import forms
from .models import *
from django.forms.models import *
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from crispy_forms.layout import *
from crispy_forms.helper import FormHelper


class CustomerForm(forms.ModelForm):
    #myservices = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,queryset = service.objects.all())
    #myservices = CServiceFormSet()
    class Meta:
        model = customer
        fields = ["name", "phonenumber"]


class CServiceForm(forms.ModelForm):
    class Meta:
        model = customerservice
        fields = ['service', 'active',]
        widgets = {
            'service': forms.Select(choices=service.objects.all()),
        }


CServiceFormSet = inlineformset_factory(customer, customerservice, CServiceForm, extra=1)

#service form
class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        exclude = ()