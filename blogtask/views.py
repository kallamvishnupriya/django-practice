from django.shortcuts import get_object_or_404, render,redirect
from .models import BlogTable

# Create your views here.
def post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            BlogTable.objects.create(title=title, description=description)
            return redirect('post')
    return render(request, 'post.html')

def home(request):
    data = BlogTable.objects.all()
    return render(request, 'home.html', {"data": data})

def read(request,id):
    read_data=get_object_or_404(BlogTable, id=id)
    return render(request,'read.html',{"read_data":read_data})

def edit(request, id):
    blog = get_object_or_404(BlogTable, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            blog.title = title
            blog.description = description
            blog.save()
            return redirect('home')
    return render(request, 'edit.html', {"blog": blog})

def delete(request,id):
    delete_data = BlogTable.request.POST.get(id=id)
    delete_data.delete()
    return redirect('home')

def back(request):
    return redirect('post')