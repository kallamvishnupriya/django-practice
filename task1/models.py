from django.db import models

# Create your models here.
class Task1(models.Model):
    task=models.CharField(max_length=50)
    def __str__(self):
        return self.task