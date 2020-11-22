from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import random
# Create your models here.
class Facility(models.Model):
    description=models.TextField()
    name=models.CharField(max_length=30)
    objects=models.Manager()
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    objects=models.Manager()
    def __str__(self):
        return self.name
class Room(models.Model):
    maxadult=models.IntegerField()
    maxchild=models.IntegerField()
    facility=models.TextField()
    roomtype=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='hotel/images')
    bed=models.IntegerField()
    description=models.TextField(default=0)
    price=models.IntegerField(default=0)
    objects=models.Manager()
    def __str__(self):
        return str(self.roomtype)
def random_string():
    return str(random.randint(1, 99999999999))
class Booking(models.Model):
    userid=models.ForeignKey(User , on_delete=models.CASCADE)
    name=models.CharField(max_length=20,default='',null=False)
    emailid=models.EmailField(default='',null=False)
    Idetitity=models.CharField(max_length=20,null=False,default='')
    BookingDate=models.DateField(max_length=20,null=False,default='')
    ArrivalDate=models.DateField(max_length=20,null=False,default='')
    DepartureDate=models.DateField(max_length=20,null=False,default='')
    gender=models.CharField(max_length=10,null=False,default='')
    address=models.CharField(max_length=100,null=False,default='')
    status=models.CharField(max_length=10,null=False,default='')
    remark=models.CharField(max_length=20,default='',null=False)
    bookingnumber=models.CharField(max_length=11,default=random_string)
    roomid=models.ForeignKey(Room,on_delete=models.CASCADE)
    objects=models.Manager()
    def __str__(self):
        return self.bookingnumber
    def get_absolute_url(self):
        return reverse('index')
class contact(models.Model):
    name=models.ForeignKey(User , on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    query=models.TextField()
    response=models.TextField(max_length=200,default='Noresponse')
    objects=models.Manager()
    def get_absolute_url(self):
        return reverse('index')
