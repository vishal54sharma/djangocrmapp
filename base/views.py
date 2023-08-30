from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpRequest
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    

    if request.method == 'POST':
       username = request.POST['username'] 
       password = request.POST['password']
       user = authenticate(request,username=username,password=password)
       if user is not  None:
           login(request, user)
           messages.success(request,"You have been logged in")
           return redirect('home')
       else:
           messages.success(request,"Oops there was an error. Please try again...")
           return redirect('home')
           
    else:
        return render(request,'home.html',{'records':records})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You ve been logged out...")
    return redirect('home')

def register_user(request):

    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request,username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request,user)
            messages.success(request,"You have successfully registered. Welcome ..")
            return redirect('home')
        else:
            messages.error(request,form.errors)
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if(request.user.is_authenticated):
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.error(request,"You must be logged in to view that page...")
        return redirect('home')
    

def delete_record(request,pk):
    if(request.user.is_authenticated):
        deleted  = Record.objects.get(id=pk)
        deleted.delete()
        messages.success(request,"Record deleted successfully...")
        return redirect('home') 
    else:
        messages.error(request,"You must be logged in to do that...")
        return redirect('home') 
    
def add_record(request):

    form  = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record added successfully...")
                return redirect('home')
        else:
            return render(request,'add_record.html',{'form':form})
    else:
        messages.error(request,"You need to log in to do that..")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form  = AddRecordForm(instance=record)
        if request.method == 'POST':
            form  = AddRecordForm(request.POST,instance=record)
            if form.is_valid():
                form.save()
                messages.success(request,"Record updated successfully...")
                return redirect('home')
        else:
            return render(request,'update_record.html',{'form':form})   
    else:
        messages.error(request,"You need to log in to do that..")
        return redirect('home')



    





