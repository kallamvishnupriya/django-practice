from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from .serializers import PersonSerializer
from .models import Person
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#apiview using with serializers
class HelloView(APIView):

    def get(self, request,id=None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # better
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        people=get_object_or_404(Person,id=id)
        serializer=PersonSerializer(people,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        people=get_object_or_404(Person,id=id)
        people.delete() 
        return Response({"message":"message is deleted successfully"})
    



# #normal views without using serializers
# @csrf_exempt
# def home_view(request):
#     if request.method=="GET":
#         people=Person.objects.all()
#         serializer = PersonSerializer(people, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         serializer = PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)

#         return JsonResponse(serializer.errors, status=400)
    

