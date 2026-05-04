from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def studentlist(request):
    if request.method=="GET":
        student_list=Student.objects.all()
        serializer=StudentSerializer(student_list, many=True)
        return Response(serializer.data )
    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET","PUT","DELETE"])
def studentlistdetails(request,id):
    try:
        student=Student.objects.get(id=id)
    except:
        return Student.DoesNotExist
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=="Delete":
        serializer=StudentSerializer(serializer)
        serializer.delete()
        return Response(serializer.data)

    




# # views.py(Class_based)
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer

# class StudentAPIView(APIView):

#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

# class StudentDetailAPIView(APIView):

#     def get_object(self, id):
#         return Student.objects.get(id=id)

#     def get(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, id):
#         student = self.get_object(id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    





# #using Generic views
# # views.py
# from rest_framework import generics
# from .models import Student
# from .serializers import StudentSerializer

# # List + Create
# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # Retrieve + Update + Delete
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# # views.py(ViewSets)      
# from rest_framework import viewsets
# from .models import Student
# from .serializers import StudentSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer