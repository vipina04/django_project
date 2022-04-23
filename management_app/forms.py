
from django import forms
from django.contrib.auth.forms import UserCreationForm
from management_app.models import Login, Worker, Complaint, Notifications, Customer


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')



class WorkerRegister(forms.ModelForm):
    class Meta:
        model =Worker
        fields = ('name', 'email', 'work_type', 'place', 'phone_number')

class CustomerRegister(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ('name', 'email', 'address','phone_number')


class ComplaintRegister(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Complaint
        fields = ('subject', 'complaint', 'date')

class Notification_add(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Notifications
        fields = ('date','subject','notification')
