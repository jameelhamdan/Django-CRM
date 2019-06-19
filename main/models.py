from django.db import models
from django.contrib import admin

class service(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):              
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=128)
    phonenumber = models.CharField(max_length=128)
    myservices = models.ManyToManyField(service, through='customerservice', through_fields=('customer', 'service'))

    def __str__(self):              
        return self.name

class customerservice(models.Model):
    customer = models.ForeignKey(customer, on_delete = models.CASCADE)
    service = models.ForeignKey(service, on_delete = models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.customer.name + " " +  self.service.name

class customerservice_inline(admin.TabularInline):
    model = customerservice
    extra = 1

class customerAdmin(admin.ModelAdmin):
    inlines = (customerservice_inline,)

