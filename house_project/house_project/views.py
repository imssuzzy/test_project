from rest_framework import generics
from .models import *
# from .serializers import CategorySerializer, PropertySerializer


class CategoryListView(generics.ListAPIView):
    model = Category
    queryset = Category.objects.all()
    # serializer_class = CategorySerializer


class PropertyListView(generics.ListAPIView):
    model = Property
    queryset = Property.objects.all()
    # serializer_class = PropertySerializer
