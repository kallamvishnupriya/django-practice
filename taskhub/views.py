from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import TaskHub


def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        User.objects.create_user(username=username,password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    return render(request,'signup.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,User)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')
    return render(request,'login.html')


@login_required
def dashboard(request):
    user = request.user
    tasks = TaskHub.objects.filter(user=user)
    total = tasks.count()
    completed = tasks.filter(is_completed='done').count()
    pending = tasks.filter(is_completed='not_yet').count()
    return render(request, 'dashboard.html', {
        'total': total,
        'completed': completed,
        'pending': pending
    })


@login_required
def tasks(request):
    user = request.user
    tasks = TaskHub.objects.filter(user=user)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


@login_required
def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        TaskHub.objects.create(
            user=request.user,
            title=title,
            description=description,
            is_completed='not_yet'
        )
        return redirect('tasks')
    return render(request, 'task_form.html')


@login_required
def task_edit(request, id):
    task = TaskHub.objects.get(id=id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.is_completed = request.POST.get("is_completed") or 'not_yet'
        task.save()
        return redirect('tasks')
    return render(request, 'task_form.html', {'task': task})


@login_required
def task_delete(request, id):
    task = TaskHub.objects.get(id=id)
    task.delete()
    return redirect('tasks')