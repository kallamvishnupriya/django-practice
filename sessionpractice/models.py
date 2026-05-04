from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Course(models.Model):
    title=models.CharField(max_length=30)
    duration=models.IntegerField()
    def __str__(self):
        return self.title
    
class Enrollement(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student.name
