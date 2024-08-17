from rest_framework import serializers
from .models import *


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'description', 'price', 'category']


class CategorySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'properties']

        