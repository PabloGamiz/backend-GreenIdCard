from tkinter import ALL
from rest_framework import serializers
from .models import (ClassificationData, ObjectData)

class ClassificationDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassificationData
        fields = ('calification','number_metrics','min_C1','max_C1','min_C2','max_C2')

class ObjectDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectData
        fields = ('object','antiquity', 'value_type', 'indicator', 'object_type', 'climatic_zone','zone', 'classification', 'value1', 'value2', 'value3')