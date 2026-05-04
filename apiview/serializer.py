from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.Serializer):
    class Meta:
        models=Student
        fields='__all__'
        