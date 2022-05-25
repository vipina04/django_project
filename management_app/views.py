from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from management_app.forms import LoginRegister, WorkerRegister, ComplaintRegister, Notification_add, CustomerRegister
from management_app.models import Complaint, Notifications, Worker, Customer


def home(request):
    return render(request, 'home.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_worker:
                return redirect('worker_home')
            elif user.is_customer:
                return redirect('customer_home')
        else:
            messages.info(request, 'INVALID CREDENTIALS')

    return render(request, 'login.html')


def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_form = WorkerRegister(request.POST)
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save(commit=False)
            user.is_worker = True
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            messages.info(request, 'worker Register Successful')
            return redirect('login')
    return render(request, 'worker_register.html', {'user_form': user_form, 'worker_form': worker_form})

def customer_register(request):
    user_form = LoginRegister()
    customer_form = CustomerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        customer_form = CustomerRegister(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, 'customer Register Successful')
            return redirect('login')
    return render(request, 'customer_register.html', {'user_form': user_form, 'customer_form': customer_form})



def complaint_add(request):
    form = ComplaintRegister()
    u = request.user
    if request.method == 'POST':
        form = ComplaintRegister(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"complaint registered successfully")
            return redirect('complaint_view')
        else:
            form = ComplaintRegister()
    return render(request, 'complaint_add.html', {'form': form})

def complaint_view(request):
    data = Complaint.objects.all()
    context = {
        'data': data
    }
    return render(request, 'complaint_view.html',context)

def admin_home(request):
    return render(request, 'admin_home.html')

def worker_home(request):
    return render(request, 'worker_home.html')

def customer_home(request):
    return render(request, 'customer_home.html')

def notification_add(request):
    form = Notification_add()
    a = request.user
    if request.method == 'POST':
        form = Notification_add(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = a
            obj.save()
            messages.info(request,"notification registered successfully")
            return redirect('notification_add')
        else:
            form = Notification_add()
    return render(request, 'notification_add.html', {'form': form})

def notification_view(request):
    data = Notifications.objects.all()
    context = {
        'data': data
    }
    return render(request, 'notification_view.html',context)
def worker_view(request):
    data = Worker.objects.all()
    context = {
        'data':data
    }
    return render(request,'worker_view.html',context)

def customer_view(request):
    data = Customer.objects.all()
    context = {
        'data':data
    }
    return render(request,'customer_view.html',context)

def update_view(request,id):
    obj = Worker.objects.get(id=id)
    form =WorkerRegister(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('worker_view')
    return render (request,'update.html',{'form':form})
def delete_worker(request,id):
    obj = Worker.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('worker_view')
    return render(request,'delete_worker.html')


def delete_customer(request,id):
    obj = Customer.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('customer_view')
    return render(request,'delete_customer.html')


def update_worker(request,id):
    obj = Worker.objects.get(id=id)
    form =WorkerRegister(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('worker_view')
    return render (request,'update_worker.html',{'form':form})

def update_customer(request,id):
    obj = Customer.objects.get(id=id)
    form =CustomerRegister(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('worker_view')
    return render (request,'update_customer.html',{'form':form})




