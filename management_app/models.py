
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Worker(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='worker')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    work_type = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=50)


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100)
    complaint = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True,blank=True)

class Notifications(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=100)
    notification = models.TextField()


