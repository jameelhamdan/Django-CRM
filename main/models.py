from django.db import models

class service(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):              
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=128)
    phonenumber = models.CharField(max_length=10)
    services = models.ManyToManyField(service, through='customerservice')

    def __str__(self):              
        return self.name

class customerservice(models.Model):
    customer = models.ForeignKey(customer, on_delete= models.CASCADE)
    service = models.ForeignKey(service, on_delete= models.CASCADE)
    active = models.BooleanField(default=True)
