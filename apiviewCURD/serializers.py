from rest_framework import serializers
from . models import ApiViewCURD

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApiViewCURD
        fields='__all__'