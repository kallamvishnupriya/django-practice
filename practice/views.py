from django.shortcuts import render
from django.http import JsonResponse
from practice.models import Hello
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def one(request):
    if request.method=="POST":
        data = json.loads(request.body)
        Hello.objects.create(
            name=data['name'],
            email=data['email'],
            number=data['number']
        )
        all_data = list(Hello.objects.values()) 
        return JsonResponse({"msg":"success","data":all_data})
    return JsonResponse({"error":"only post"})

@csrf_exempt
def two(request,id):
    if request.method=="GET":
        data=Hello.objects.get(id=id)
        return JsonResponse({
            "msg": "success",
            "data": {
                "id": data.id,
                "name": data.name,
                "email": data.email,
                "number": data.number
            }
        })
    return JsonResponse({"msg":"failed to fetch"})