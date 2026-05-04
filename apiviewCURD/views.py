from django.shortcuts import render
from . serializers import ItemSerializer
from .models import ApiViewCURD 
from rest_framework.views import APIView
from rest_framework.response import Response


class ItemList(APIView):
    def get(self,request):
        items= ApiViewCURD.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data)
