from itertools import count

from django.views import View
from .models import (ClassificationResidentialBuilding, ClassificationNotResidentialBuilding, NewBuildingDemand, NewBuildingEnergyConsume, NewBuildingEmissions, ExistingBuildingDemand, ExistingBuildingEnergyConsume, ExistingBuildingEmissions, NewBuldingDemandDispersions, NewBuldingEnergyAndEmissionsDispersions, ExistingBuldingDemandDispersions, ExistingBuldingEnergyAndEmissionsDispersions,SystemUser,File,Calcul, BuildingValues, SoftwareValues, ClassificationData, ObjectData)
from .serializers import (ClassificationResidentialBuildingSerializer, ClassificationNotResidentialBuildingSerializer, NewBuildingDemandSerializer, NewBuildingEnergyConsumeSerializer, NewBuildingEmissionsSerializer, ExistingBuildingDemandSerializer, ExistingBuildingEnergyConsumeSerializer, ExistingBuildingEmissionsSerializer, NewBuldingDemandDispersionsSerializer, NewBuldingEnergyAndEmissionsDispersionsSerializer, ExistingBuldingDemandDispersionsSerializer, ExistingBuldingEnergyAndEmissionsDispersionsSerializer, SystemUserSerializer,FileSerializer,CalculSerializer,BuildingValuesSerializer,SoftwareValuesSerializer,ClassificationDataSerializer, ObjectDataSerializer)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

class ResidentialBuildingClassificationSet(ViewSet):

    @api_view(['DELETE'])
    def deleteallobjects(request):
        ClassificationResidentialBuilding.objects.all().delete()
        ClassificationNotResidentialBuilding.objects.all().delete()
        NewBuildingDemand.objects.all().delete()
        NewBuildingEnergyConsume.objects.all().delete()
        NewBuildingEmissions.objects.all().delete()
        ExistingBuildingDemand.objects.all().delete()
        ExistingBuildingEnergyConsume.objects.all().delete()
        ExistingBuildingEmissions.objects.all().delete()
        NewBuldingDemandDispersions.objects.all().delete()
        NewBuldingEnergyAndEmissionsDispersions.objects.all().delete()
        ExistingBuldingDemandDispersions.objects.all().delete()
        ExistingBuldingEnergyAndEmissionsDispersions.objects.all().delete()
        return Response(status = status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def residentialBuildingClassification(request):
        serializer = ClassificationResidentialBuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_404_NOT_FOUND)

    @api_view(['PUT', 'DELETE'])
    def updateRBClassification(request, classification):
        try:
            classification = ClassificationResidentialBuilding.objects.get(calification = classification)
        except ClassificationResidentialBuilding.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ClassificationResidentialBuildingSerializer(classification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            classification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    @api_view(['GET'])
    def getRBClassificationC1(request, C1):
            try:
                classification = ClassificationResidentialBuilding.objects.get(min_C1__lte = C1, max_C1__gt=C1)
            except ClassificationResidentialBuilding.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassificationResidentialBuildingSerializer(classification)
            return Response(serializer.data, status = status.HTTP_200_OK)

    @api_view(['GET'])
    def getRBClassificationC1C2(request, C1, C2):
            try:
                classification = ClassificationResidentialBuilding.objects.filter(min_C1__lte = C1, max_C1__gt = C1, min_C2__lte =C2, max_C2__gt = C2)
            except ClassificationResidentialBuilding.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassificationResidentialBuildingSerializer(classification)
            return Response(serializer.data, status = status.HTTP_200_OK)



class NonResidentialBuildingSet(ViewSet):

    @api_view(['POST'])
    def nonresidentialBuildingClassification(request):
        serializer = ClassificationNotResidentialBuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT', 'DELETE'])
    def updateNRBClassification(request, classification):
        try:
            classification = ClassificationNotResidentialBuilding.objects.get(calification = classification)
        except ClassificationNotResidentialBuilding.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ClassificationNotResidentialBuildingSerializer(classification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            classification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    @api_view(['GET'])
    def getNRBClassificationC(request, C):
            try:
                classification = ClassificationNotResidentialBuilding.objects.get(min_C__lt = C, max_C__gt=C)
            except ClassificationNotResidentialBuilding.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassificationNotResidentialBuildingSerializer(classification)
            return Response(serializer.data, status = status.HTTP_200_OK)
        

class NewBuildingDemandSet(ViewSet):

    @api_view(['POST'])
    def newBuildingDemand(request):
        serializer = NewBuildingDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateNBDemand(request, type, zone):
        try:
            demand = NewBuildingDemand.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingDemand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = NewBuildingDemandSerializer(demand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            demand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = NewBuildingDemandSerializer(demand)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getNBDemand(request, type, zone):
        try:
            demand = NewBuildingDemand.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingDemand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewBuildingDemandSerializer(demand, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class NewBuildingEnergyConsumptionSet(ViewSet):

    @api_view(['POST'])
    def newBuildingEnergyConsumption(request):
        serializer = NewBuildingEnergyConsumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateNBEnergyConsumption(request, type, zone):
        try:
            ec = NewBuildingEnergyConsume.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingEnergyConsume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = NewBuildingEnergyConsumeSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = NewBuildingEnergyConsumeSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getNBEnergyConsumption(request, type, zone):
        try:
            ec = NewBuildingEnergyConsume.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingEnergyConsume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewBuildingEnergyConsumeSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)


class NewBuildingEmissionsSet(ViewSet):
    
    @api_view(['POST'])
    def newBuildingEmissions(request):
        serializer = NewBuildingEmissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateNBEmissions(request, type, zone):
        try:
            ec = NewBuildingEmissions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingEmissions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = NewBuildingEmissionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = NewBuildingEmissionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getNBEmissions(request, type, zone):
        try:
            ec = NewBuildingEmissions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuildingEmissions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewBuildingEmissionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    

class ExistingBuildingDemandSet (ViewSet):

    @api_view(['POST'])
    def existingBuildingDemand(request):
        serializer = ExistingBuildingDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateEBDemand(request, type, zone):
        try:
            d = ExistingBuildingDemand.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingDemand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ExistingBuildingDemandSerializer(d, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            d.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ExistingBuildingDemandSerializer(d)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getEBDemand(request, type, zone):
        try:
            d = ExistingBuildingDemand.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingDemand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExistingBuildingDemandSerializer(d)
        return Response(serializer.data, status = status.HTTP_200_OK)

    
class ExistingBuildingEnergyConsumptionSet(ViewSet):

    @api_view(['POST'])
    def existingBuildingEnergyConsumption(request):
        serializer = ExistingBuildingEnergyConsumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateEBEnergyConsumption(request, type, zone):
        try:
            ec = ExistingBuildingEnergyConsume.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingEnergyConsume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ExistingBuildingEnergyConsumeSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ExistingBuildingEnergyConsumeSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getEBEnergyConsumption(request, type, zone):
        try:
            ec = ExistingBuildingEnergyConsume.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingEnergyConsume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExistingBuildingEnergyConsumeSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class ExistingBuildingEmissionsSet(ViewSet):

    @api_view(['POST'])
    def existingBuildingEmissions(request):
        serializer = ExistingBuildingEmissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateEBEmissions(request, type, zone):
        try:
            ec = ExistingBuildingEmissions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingEmissions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ExistingBuildingEmissionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ExistingBuildingEmissionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getEBEmissions(request, type, zone):
        try:
            ec = ExistingBuildingEmissions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuildingEmissions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExistingBuildingEmissionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)


class NewBuildingDemandDispersionsSet (ViewSet):


    @api_view(['POST'])
    def newBuildingDemandDispersions(request):
        serializer = NewBuldingDemandDispersionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateNBDemandDispersions(request, type, zone):
        try:
            ec = NewBuldingDemandDispersions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuldingDemandDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = NewBuldingDemandDispersionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = NewBuldingDemandDispersionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getNBDemandDispersions(request, type, zone):
        try:
            ec = NewBuldingDemandDispersions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuldingDemandDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewBuldingDemandDispersionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    

class NewBuildingEnergyAndEmissionsDispersionsSet(ViewSet):

    @api_view(['POST'])
    def newBuildingEnergyAndEmissionsDispersions(request):
        serializer = NewBuldingEnergyAndEmissionsDispersionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateNBEnergyAndEmissionsDispersions(request, type, zone):
        try:
            ec = NewBuldingEnergyAndEmissionsDispersions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuldingEnergyAndEmissionsDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = NewBuldingEnergyAndEmissionsDispersionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = NewBuldingEnergyAndEmissionsDispersionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getNBEnergyAndEmissionsDispersions(request, type, zone):
        try:
            ec = NewBuldingEnergyAndEmissionsDispersions.objects.get(building_type=type, climatic_zone=zone)
        except NewBuldingEnergyAndEmissionsDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewBuldingEnergyAndEmissionsDispersionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    


class ExistingBuildingDemandDispersionsSet (ViewSet):

    @api_view(['POST'])
    def existingBuildingDemandDispersions(request):
        serializer = ExistingBuldingDemandDispersionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE','GET'])
    def updateEBDemandDispersions(request, type, zone):
        try:
            ec = ExistingBuldingDemandDispersions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuldingDemandDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ExistingBuldingDemandDispersionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ExistingBuldingDemandDispersionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getEBDemandDispersions(request, type, zone):
        try:
            ec = ExistingBuldingDemandDispersions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuldingDemandDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExistingBuldingDemandDispersionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class ExistingBuildingEnergyAndEmissionsDispersionsSet(ViewSet):

    @api_view(['POST'])
    def existingBuildingEnergyAndEmissionsDispersions(request):
        serializer = ExistingBuldingEnergyAndEmissionsDispersionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT','DELETE','GET'])
    def updateEBEnergyAndEmissionsDispersions(request, type, zone):
        try:
            ec = ExistingBuldingEnergyAndEmissionsDispersions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuldingEnergyAndEmissionsDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = ExistingBuldingEnergyAndEmissionsDispersionsSerializer(ec, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ec.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = ExistingBuldingEnergyAndEmissionsDispersionsSerializer(ec)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getEBEnergyAndEmissionsDispersions(request, type, zone):
        try:
            ec = ExistingBuldingEnergyAndEmissionsDispersions.objects.get(building_type=type, climatic_zone=zone)
        except ExistingBuldingEnergyAndEmissionsDispersions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExistingBuldingEnergyAndEmissionsDispersionsSerializer(ec, data=request.data)
        return Response(serializer.data, status = status.HTTP_200_OK)

class FileView(ViewSet):

    @swagger_auto_schema(
        operation_description='Crea un fitxer', 
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='Proporciona el nom del fitxer, la seva descripcio i l\'usuari al que pertany',
            properties= {
                'name': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona el nom',
                                    example= 'username'),
                'description': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona la descripcio',
                                    example= 'descripcio d\'exemple'),
                'username': openapi.Schema(type=openapi.TYPE_STRING,
                                    format=openapi.FORMAT_FLOAT,
                                    description='Proporciona el nom d\'usuari',
                                    example= 'exemple'),
            },
            required=["name", "description", "username"],
        ),
        responses= {401: 'You provided no api key', 404: 'contribution not found', 200: 'Dispersions d\'energia i dimensions creades correctament'})
    def create(self, request, pk=None):
        u = File(name=request.data['name'], description=request.data['description'], username=request.data['username'])
        serializer = FileSerializer(u)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description='Actualitza la informació d\'un usuari', 
        manual_parameters=[
            openapi.Parameter(
                'name',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                required=True,
                description='Proporciona el nom',
            ),
            openapi.Parameter(
                'descripcio',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                required=True,
                description='Proporciona la descripcio',
            ),
        ],
        responses= {401: 'You provided no api key', 404: 'contribution not found', 200: 'Dispersions d\'energia i dimensions creades correctament'})
    def update(self, request):
        u = File.objects.filter(name = request.data['name'], descripcio = request.data['descripcio'])
        u.password = request.data['password']
        u.save()
        serializer = FileSerializer(u)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description='Esborra un fitxer', 
        responses= {401: 'You provided no api key', 404: 'contribution not found', 200: 'Dispersions d\'energia i dimensions creades correctament'})
    def delete(self, request, pk=None):
        u = File.objects.filter(pk = pk)
        result = u.delete()
        return Response(result)


class CalculSet(ViewSet):

    @swagger_auto_schema(
        operation_description='Crea un calcul', 
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='Proporciona el tipus, data, valor, calificacio, consum i fitxer del calcul',
            properties= {
                'type': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona el tipus',
                                    example= 'username'),
                'date': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona la data',
                                    example= '21/02/2022'),
                'value': openapi.Schema(type=openapi.TYPE_STRING,
                                    format=openapi.FORMAT_FLOAT,
                                    description='Proporciona el valor del calcul',
                                    example= 1.5),
                'calification': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona la calificacio del calcul',
                                    example= 'A'),
                'consumption': openapi.Schema(type=openapi.TYPE_STRING,
                                    format=openapi.FORMAT_FLOAT,
                                    description='Proporciona el valor del consum',
                                    example= 1.5),
                'file': openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Proporciona el id del fitxer',
                                    example= '3g4v456gv'),          
            },
            required=["type", "date", "value","calification","consumption","file"],
        ),
        responses= {401: 'You provided no api key', 404: 'contribution not found', 200: 'Dispersions d\'energia i dimensions creades correctament'})
    def create(self, request, pk=None):
        c = Calcul(type=request.data['type'], date=request.data['date'], value=request.data['value'],calification=request.data['calification'], consumption=request.data['consumption'], file=request.data['file'])
        serializer = CalculSerializer(c)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description='Esborra un fitxer', 
        manual_parameters=[
            openapi.Parameter(
                'id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                required=True,
                description='Proporciona l\'usuari a esborrar',
            ),
        ],
        responses= {401: 'You provided no api key', 404: 'contribution not found', 200: 'Dispersions d\'energia i dimensions creades correctament'})
    def delete(self, request):
        c = Calcul.objects.filter(name = request.data['id'])
        result = c.delete()
        return Response(result)

class BuildingValuesSet(ViewSet):

    @api_view(['POST'])
    def BuildingValue(self, request):
        serializer = BuildingValuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['UPDATE', 'DELETE', 'GET'])
    def ModifyBuildingValues (self, request, antiquity, value_type, indicator, building_type, climatic_zone):
        try:
            bv = BuildingValues.objects.get(antiquity=antiquity, value_type=value_type, indicator=indicator, building_type=building_type, climatic_zone=climatic_zone)
        except BuildingValues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = BuildingValuesSerializer(bv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            bv.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = BuildingValuesSerializer(bv)
            return Response(serializer.data, status = status.HTTP_200_OK)

class SoftwareValuesSet(ViewSet):

    @api_view(['POST'])
    def SoftwareValue(self, request):
        serializer = SoftwareValuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['UPDATE', 'DELETE', 'GET'])
    def ModifySoftwareValues (self, request, part_type, name):
        try:
            sv = SoftwareValues.objects.get(part_type=part_type, name=name)
        except SoftwareValues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = SoftwareValuesSerializer(sv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            sv.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = SoftwareValuesSerializer(sv)
            return Response(serializer.data, status = status.HTTP_200_OK)

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
            print(count_classifications)
            if count_classifications == 1:
                print('dentro de 1')
                try:
                    classification = ClassificationData.objects.get(number_metrics = number_metrics, min_C1__lte = C1, max_C1__gt=C1)
                except ClassificationData.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ClassificationDataSerializer(classification)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                print('dentro de 2')
                try:
                    classification = ClassificationData.objects.get(number_metrics = number_metrics,min_C1__lte = C1, max_C1__gt = C1, min_C2__lte =C2, max_C2__gt = C2)
                except ClassificationData.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ClassificationDataSerializer(classification)
                return Response(serializer.data, status = status.HTTP_200_OK)


class CalculationDataSet(ViewSet):

    @api_view(['POST'])
    def createCalculationData(request):
        print(request)
        serializer = ObjectDataSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print('dentro de valido')
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
    def getCPUs(request, object_type):
        bv = ObjectData.objects.filter(object_type=object_type).count()
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


class UserViewSet(ViewSet):

    @api_view(['POST'])
    def createUser(request):
        serializer = SystemUserSerializer(data=request.data)
        print(serializer)
        print('despues de serializer')
        if serializer.is_valid():
            print('es valido')
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE', 'GET'])
    def modifyUser(request, email):
        try:
            u = SystemUser.objects.get(email = email)
        except SystemUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = SystemUserSerializer(u, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            u.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = SystemUserSerializer(u)
            return Response(serializer.data, status = status.HTTP_200_OK)


class FileViewSet(ViewSet):

    @api_view(['POST'])
    def createFile(request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE', 'GET'])
    def modifyFile(request, id):
        try:
            u = File.objects.get(id = id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = FileSerializer(u, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            u.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = FileSerializer(u)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getFiles(request, userId):
        try:
            u = File.objects.get(User = userId)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(u)
        return Response(serializer.data, status = status.HTTP_200_OK)

class CalculViewSet(ViewSet):

    @api_view(['POST'])
    def createCalcul(request):
        serializer = CalculSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PUT', 'DELETE', 'GET'])
    def modifyCalcul(request, email):
        try:
            u = Calcul.objects.get(email = email)
        except Calcul.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = CalculSerializer(u, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            u.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET': 
            serializer = CalculSerializer(u)
            return Response(serializer.data, status = status.HTTP_200_OK)

    @api_view(['GET'])
    def getCalculs(request, fileId):
        try:
            u = Calcul.objects.get(File = fileId)
        except Calcul.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CalculSerializer(u)
        return Response(serializer.data, status = status.HTTP_200_OK)
