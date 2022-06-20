from itertools import count

from django.views import View
from .models import (ClassificationData, ObjectData)
from .serializers import (ClassificationDataSerializer, ObjectDataSerializer)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status


class ClassificationDataSet(ViewSet):

    @api_view(['POST'])
    def createClassification(request):
        serializer = ClassificationDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_404_NOT_FOUND)

    @api_view(['PUT', 'DELETE'])
    def updateClassification(request, number_metrics, classification):
        try:
            classification = ClassificationData.objects.get(number_metrics = number_metrics, calification = classification)
        except ClassificationData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ClassificationDataSerializer(classification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            classification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    @api_view(['GET'])
    def getClassificationC(request, number_metrics, C):
            try:
                classification = ClassificationData.objects.get(number_metrics = number_metrics, min_C1__lte = C, max_C1__gt=C)
            except ClassificationData.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassificationDataSerializer(classification)
            return Response(serializer.data, status = status.HTTP_200_OK)

    @api_view(['GET'])
    def getClassificationC1C2(request, number_metrics, C1, C2):

            count_classifications = ClassificationData.objects.filter(number_metrics = number_metrics, min_C1__lte = C1, max_C1__gt = C1).count()
            if count_classifications == 1:
                try:
                    classification = ClassificationData.objects.get(number_metrics = number_metrics, min_C1__lte = C1, max_C1__gt=C1)
                except ClassificationData.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ClassificationDataSerializer(classification)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                try:
                    classification = ClassificationData.objects.get(number_metrics = number_metrics,min_C1__lte = C1, max_C1__gt = C1, min_C2__lte =C2, max_C2__gt = C2)
                except ClassificationData.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ClassificationDataSerializer(classification)
                return Response(serializer.data, status = status.HTTP_200_OK)


class CalculationDataSet(ViewSet):

    @api_view(['POST'])
    def createCalculationData(request):
        serializer = ObjectDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE', 'GET'])
    def ModifyBuildingData (request, object, antiquity, value_type, indicator, object_type, climatic_zone, zone):
        try:
            bv = ObjectData.objects.get(object = object, antiquity=antiquity, value_type=value_type, indicator=indicator, object_type=object_type, climatic_zone=climatic_zone, zone=zone)
        except ObjectData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        if request.method == 'PUT':
            serializer = ObjectDataSerializer(bv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            bv.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ObjectDataSerializer(bv)
            return Response(serializer.data, status = status.HTTP_200_OK)

    @api_view(['GET'])
    def getBuildingMaximumValue(request, object, antiquity, value_type, indicator, object_type, climatic_zone, zone, classification):
        try:
            bv = ObjectData.objects.get(object = object, antiquity=antiquity, value_type=value_type, indicator=indicator, object_type=object_type, climatic_zone=climatic_zone, zone=zone, classification=classification)
        except ObjectData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        serializer = ObjectDataSerializer(bv)
        return Response(serializer.data, status = status.HTTP_200_OK)


    @api_view(['PUT', 'DELETE', 'GET'])
    def ModifySoftwareData (request, object, object_type, value_type):
        try:
            bv = ObjectData.objects.get(object = object, value_type=value_type, object_type=object_type)
        except ObjectData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ObjectDataSerializer(bv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            bv.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ObjectDataSerializer(bv)
            return Response(serializer.data, status = status.HTTP_200_OK)

    @api_view(['GET'])
    def getCPUs(request, object, object_type):
        bv = ObjectData.objects.filter(object=object, object_type=object_type).count()
        if bv > 1:
            try: 
                bv = ObjectData.objects.filter(object_type=object_type)
            except ObjectData.DoesNotExist:    
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ObjectDataSerializer(bv, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            try: 
                bv = ObjectData.objects.get(object_type=object_type)
            except ObjectData.DoesNotExist:    
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ObjectDataSerializer(bv)
            return Response(serializer.data, status = status.HTTP_200_OK)