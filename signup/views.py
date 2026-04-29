from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user :
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login.html',{"error":'invalid crendials'})
    return render(request,'login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
