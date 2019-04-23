"""
it validates the model queryset and produces Pythonic data type to work with.
ModelSerializer for our puppy model, validating all the mentioned fields.
In short, if you have a one-to-one relationship between your API endpoints and
your models - which you probably should if you’re creating 
a RESTful API - then you can use a ModelSerializer to create a Serializer.
"""

from rest_framework import serializers
from .models import Puppy

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')
