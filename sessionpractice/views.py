from django.shortcuts import redirect, render
from sessionpractice.models import Student,Course,Enrollement

def create_enroll(request,sid,cid):
    student=Student.objects.get(id=sid)
    course=Course.objects.get(id=cid)
    Enrollement.objects.create(student=student,course=course)
    return redirect('/sessionpractice/show-enrollments/')

def show_enrollements(request):
    data=Enrollement.objects.all()
    return render(request,"index.html",{"enroll":data})