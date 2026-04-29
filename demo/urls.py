from django.contrib import admin
from django.urls import include, path
from StudentRecord.views import create,student_list,delete_student,get_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice/',include('practice.urls')),
    path('sessionpractice/',include('sessionpractice.urls')),
    path('taskhub/',include('taskhub.urls')),
    path('mini/',include('miniproj.urls')),
    path('signup/',include('signup.urls')),
    path('contact/',include('contact.urls')),
    path('student_form/',create , name='student_form'),
    path('students/', student_list, name='student_list'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('get_student/<int:id>/',get_student,name='get_student'),
]