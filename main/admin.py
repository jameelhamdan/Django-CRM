from django.contrib import admin
from .models import *
   
admin.site.register(service)
admin.site.register(customer, customerAdmin)
