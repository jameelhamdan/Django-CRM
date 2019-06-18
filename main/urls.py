from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'), 
    #services
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.services, name='services'), 
    #customers
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.customers, name='customers'),
    path('customer/add/', views.customersadd, name='customeradd'),
    path('customer/delete/<int:customer_id>', views.customersdelete, name='customerdelete'),
    #path('customers/<int:customer_id>/services', views.services, name='services'),
    
]
