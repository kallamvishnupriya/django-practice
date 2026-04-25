from django.contrib import admin
from django.urls import path
from StudentRecord.views import create,student_list,delete_student,get_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_form/',create , name='student_form'),
    path('students/', student_list, name='student_list'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('get_student/<int:id>/',get_student,name='get_student'),
]