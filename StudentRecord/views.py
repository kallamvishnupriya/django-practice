from django.shortcuts import get_object_or_404, redirect, render
from StudentRecord.models import student_record
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create(request):
    if request.method == "POST":
        student_record.objects.create(
            name=request.POST['name'],
            roll_number=request.POST['roll_number'],
            email=request.POST['email'],
            course=request.POST['course'],
            admission_date=request.POST['admission_date']
        )
        return redirect('student_list')   
    return render(request, 'form.html')

def student_list(request):
    data = student_record.objects.all()
    return render(request, 'show.html', {'data': data})

def delete_student(request, id):
    student = get_object_or_404(student_record, id=id)
    student.delete()
    return redirect('student_list')

def get_student(request,id):
    get_data=student_record.objects.get(id=id)
    return render(request,'get_data.html',{'get_data':get_data})