from django.db import models

# Create your models here.
class TaskHub(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('not_yet', 'Not Yet'),
    ]
    is_completed=models.CharField(max_length=10,choices=STATUS_CHOICES,default='not_yet')
    