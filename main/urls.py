from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'), 
    #services
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.services, name='services'), 
    path('service/add/', views.servicesadd, name='serviceadd'),
    path('service/delete/<int:service_id>', views.servicesdelete, name='servicedelete'),


    #customers
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.customers, name='customers'),
    path('customer/add/', views.customeradd, name='customeradd'),
    path('customer/edit/<int:pk>/', views.customeredit, name='customeredit'),
    path('customer/delete/<int:customer_id>', views.customersdelete, name='customerdelete'),
    #path('customers/<int:customer_id>/services', views.services, name='services'),
    
]
