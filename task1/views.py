from django.shortcuts import render,redirect
from .models import Task1

# Create your views here.
def task1(request):
    if request.method=="POST":
        task=request.POST.get("task")
        if task:
            Task1.objects.create(task=task)
        return redirect('task1')
    data=Task1.objects.all()
    return render(request,'index.html',{"data":data})

def delete_task1(request,id):
    task=Task1.objects.get(id=id)
    task.delete()
    return redirect('task1')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task1

def edit_task(request, id):
    task = Task1.objects.get(id=id)
    if request.method == "POST":
        edittask = request.POST.get("edittask")
        if edittask:
            task.task = edittask
            task.save()
        return redirect('task1')
    return render(request, 'edit.html', {'task': task})