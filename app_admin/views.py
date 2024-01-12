from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from app_user.models import *
import random

# Create your views here.

def start_up(request):
    return render(request,'admin/start_up.html')

def shows_guest(request):
    shows=ShowTb.objects.filter()
    return render(request,'admin/shows.html',{'see':shows})

def show_details_guest(request,id):
    details=ShowTb.objects.filter(id=id)
    return render(request,'admin/show_details.html',{'see':details})

def news(request):
    return render(request,'admin/news.html')

def register(request):
    return render(request,'admin/register.html')

def registeraction(request):
    name=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mobile']
    password=request.POST['password']
    conf_password=request.POST['confirm_password']
    if password == conf_password:
        register_me = RegisterTb(name=name,email=email,mobile=mobile,password=password)
        register_me.save()
        messages.add_message(request,messages.INFO,"Account Created Successfully.")
    else:
        messages.add_message(request,messages.INFO,"Confirm password doesn't matches with password entered.")

    return render(request,'admin/start_up.html')

def sign_in(request):
    return render(request,'admin/sign_in.html')

def sign_inaction(request):
    user_id=request.POST['user_id']
    mobile=request.POST['user_id']
    password=request.POST['password']
    check_user=RegisterTb.objects.filter(email=user_id,password=password) | RegisterTb.objects.filter(mobile=mobile,password=password)
    if check_user.count()>0:        
        request.session['yourself']=check_user[0].id
        reviews=ReviewTb.objects.order_by('-time')[:1]
        return render(request,'user/home.html',{'see':check_user,'post':reviews})
    else:
        messages.add_message(request,messages.INFO,"Wrong Credentials, check your User Name or Password")
        return render(request,'admin/start_up.html')
