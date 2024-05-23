from rest_framework import serializers
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'     

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
     