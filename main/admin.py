from django.contrib import admin
from .models import customer
from .models import service

# Register your models here.
admin.site.register(customer)
admin.site.register(service)
