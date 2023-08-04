from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import profile

def login_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.error(request, 'Account not found')
            return HttpResponseRedirect(request.path_info)
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request,'your email is not verified')
            return HttpResponseRedirect(request.path_info)
        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        
        messages.warning(request,'Invalid credential')
        return HttpResponseRedirect(request.path_info)
    return render(request,"accounts/login.html")

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user_obj=User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.warning(request, 'Email is already taken')
            return HttpResponseRedirect(request.path_info)
        
        print(email)
        user_obj=User.objects.create(first_name=first_name , last_name=last_name , email=email , username=email)
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request,'An Email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    
    
    return render(request,'accounts/register.html')

def activate_mail(request,email_token):
    try:
        user=profile.objects.get(email_token=email_token)
        user.is_email_verified=True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token')


def cart(request):
    return render(request, "accounts/cart.html")
    






# Create your views here.
