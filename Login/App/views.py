from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        new_user = User(fname=fname,lname=lname,email=email,password=password,phone=phone)
        new_user.save()
        return redirect('login')

    return render(request,'register.html')

def Login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return HttpResponse("Login Sucessfully!!")
        else:
            return HttpResponse("Error! User doesn't exists!!")       
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('login')