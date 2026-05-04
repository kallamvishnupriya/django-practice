from django.db import models

class student_record(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    email=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    admission_date=models.DateField()
    def __str__(self):
        return self.name
