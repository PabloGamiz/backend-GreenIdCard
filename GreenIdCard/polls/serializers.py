from tkinter import ALL
from rest_framework import serializers
from .models import (BuildingValues, ClassificationResidentialBuilding, ClassificationNotResidentialBuilding, NewBuildingDemand, NewBuildingEnergyConsume, NewBuildingEmissions, ExistingBuildingDemand, ExistingBuildingEnergyConsume, ExistingBuildingEmissions, NewBuldingDemandDispersions, NewBuldingEnergyAndEmissionsDispersions, ExistingBuldingDemandDispersions, ExistingBuldingEnergyAndEmissionsDispersions, SoftwareValues, SystemUser, File, Calcul, ClassificationData, ObjectData)


class ClassificationResidentialBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationResidentialBuilding
        fields = ['calification','min_C1','max_C1','min_C2','max_C2']


class ClassificationNotResidentialBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationNotResidentialBuilding
        fields = ('calification','min_C','max_C')

class NewBuildingDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBuildingDemand
        fields = ('building_type','climatic_zone','heating','refrigeration')

class NewBuildingEnergyConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBuildingEnergyConsume
        fields = ('building_type','climatic_zone','heating','refrigeration','ACS')

class NewBuildingEmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBuildingEmissions
        fields = ('building_type','climatic_zone','heating','refrigeration','ACS')

class ExistingBuildingDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingBuildingDemand
        fields = ('building_type','climatic_zone','heating','refrigeration')

class ExistingBuildingEnergyConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingBuildingEnergyConsume
        fields = ('building_type','climatic_zone','heating','refrigeration','ACS')

class ExistingBuildingEmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingBuildingEmissions
        fields = ('building_type','climatic_zone','heating','refrigeration','ACS')

class NewBuldingDemandDispersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBuldingDemandDispersions
        fields = ('building_type','climatic_zone','dispersion')

class NewBuldingEnergyAndEmissionsDispersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBuldingEnergyAndEmissionsDispersions
        fields = ('building_type','climatic_zone','dispersion')

class ExistingBuldingDemandDispersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingBuldingDemandDispersions
        fields = ('building_type','climatic_zone','dispersion')

class ExistingBuldingEnergyAndEmissionsDispersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingBuldingEnergyAndEmissionsDispersions
        fields = ('building_type','climatic_zone','dispersion')

class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('id', 'email', 'name','surname', 'password')

class FileSerializer(serializers.ModelSerializer):
    #user = SystemUserSerializer(read_only=True)
    class Meta:
        model = File
        fields = ('id','name', 'description', 'user')

class CalculSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    class Meta:
        model = Calcul
        fields = ('id','type', 'date','file','value11','calification11','value12','calification12','value13','calification13','value21','calification21','value22','calification22','value23','calification23','value31','calification31','value32','calification32','value33','calification33')

class BuildingValuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingValues
        fields = ('antiquity', 'value_type', 'indicator', 'building_type', 'climatic_zone', 'value1', 'value2', 'value3')

class SoftwareValuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareValues
        fields = ('part_type', 'name', 'core_number', 'consumption')

class ClassificationDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassificationData
        fields = ('calification','number_metrics','min_C1','max_C1','min_C2','max_C2')

class ObjectDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectData
        fields = ('object','antiquity', 'value_type', 'indicator', 'object_type', 'climatic_zone','zone', 'classification', 'value1', 'value2', 'value3')