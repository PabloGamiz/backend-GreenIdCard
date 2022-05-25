from django.contrib import admin
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from . import views

from django.urls import path, register_converter

from . import converts, views

register_converter(converts.FloatUrlParameterConverter, 'float')

#router = SimpleRouter()

#router.register(r'residentialBuildingClassification', views.ResidentialBuildingClassificationSet, 'residentialBuildingClassification')
#router.register(r'nonResidentialBuildingClassification', views.NonResidentialBuildingSet, 'nonResidentialBuildingClassification')
#router.register(r'newBuildingDemand', views.NewBuildingDemandSet, 'newBuildingDemand')
#router.register(r'newBuildingEnergyConsumption', views.NewBuildingEnergyConsumptionSet, 'newBuildingEnergyConsumption')
#router.register(r'newBuildingEmissions', views.NewBuildingEmissionsSet, 'newBuildingEmissions')
#router.register(r'existingBuildingDemand', views.ExistingBuildingDemandSet, 'existingBuildingDemand')
#router.register(r'existingBuildingEnergyConsumption', views.ExistingBuildingEnergyConsumptionSet, 'existingBuildingEnergyConsumption')
#router.register(r'existingBuildingEmissions', views.ExistingBuildingEmissionsSet, 'existingBuildingEmissions')
#router.register(r'newBuildingDemandDispersions', views.NewBuildingDemandDispersionsSet, 'newBuildingDemandDispersions')
#router.register(r'newBuildingEnergyAndEmissionsDispersions', views.NewBuildingEnergyAndEmissionsDispersionsSet, 'newBuildingEnergyAndEmissionsDispersions')
#router.register(r'existingBuildingDemandDispersions', views.ExistingBuildingDemandDispersionsSet, 'existingBuildingDemandDispersions')
#router.register(r'exisitingBuildingEnergyAndEmissionsDispersions', views.ExistingBuildingEnergyAndEmissionsDispersionsSet, 'existingBuildingEnergyAndEmissionsDispersions')


urlpatterns =[
    path('deleteobjects/', views.ResidentialBuildingClassificationSet.deleteallobjects),
    path('residentialBuildingClassification/', views.ResidentialBuildingClassificationSet.residentialBuildingClassification),
    path('residentialBuildingClassification/<str:classification>/', views.ResidentialBuildingClassificationSet.updateRBClassification),
    path('residentialBuildingClassificationC1/<float:C1>/', views.ResidentialBuildingClassificationSet.getRBClassificationC1),
    path('residentialBuildingClassificationC1C2/<float:C1>/<float:C2>/', views.ResidentialBuildingClassificationSet.getRBClassificationC1C2),
    path('nonresidentialBuildingClassification/', views.NonResidentialBuildingSet.nonresidentialBuildingClassification),
    path('nonresidentialBuildingClassification/<str:classification>/', views.NonResidentialBuildingSet.updateNRBClassification),
    path('nonresidentialBuildingClassificationC/<float:C>/', views.NonResidentialBuildingSet.getNRBClassificationC),
    path('newBuildingDemand/', views.NewBuildingDemandSet.newBuildingDemand),
    path('newBuildingDemand/<str:type>/<str:zone>/', views.NewBuildingDemandSet.updateNBDemand),
    path('newBuildingDemand/<str:type>/<str:zone>/', views.NewBuildingDemandSet.getNBDemand),
    path('newBuildingEnergyConsumption/', views.NewBuildingEnergyConsumptionSet.newBuildingEnergyConsumption),
    path('newBuildingEnergyConsumption/<str:type>/<str:zone>/', views.NewBuildingEnergyConsumptionSet.updateNBEnergyConsumption),
    path('newBuildingEnergyConsumption/<str:type>/<str:zone>/', views.NewBuildingEnergyConsumptionSet.getNBEnergyConsumption),
    path('newBuildingEmissions/', views.NewBuildingEmissionsSet.newBuildingEmissions),
    path('newBuildingEmissions/<str:type>/<str:zone>/', views.NewBuildingEmissionsSet.updateNBEmissions),
    path('newBuildingEmissions/<str:type>/<str:zone>/', views.NewBuildingEmissionsSet.getNBEmissions),
    path('existingBuildingDemand/', views.ExistingBuildingDemandSet.existingBuildingDemand),
    path('existingBuildingDemand/<str:type>/<str:zone>/', views.ExistingBuildingDemandSet.updateEBDemand),
    path('existingBuildingDemand/<str:type>/<str:zone>/', views.ExistingBuildingDemandSet.getEBDemand),
    path('existingBuildingEnergyConsumption/', views.ExistingBuildingEnergyConsumptionSet.existingBuildingEnergyConsumption),
    path('existingBuildingEnergyConsumption/<str:type>/<str:zone>/', views.ExistingBuildingEnergyConsumptionSet.updateEBEnergyConsumption),
    path('existingBuildingEnergyConsumption/<str:type>/<str:zone>/', views.ExistingBuildingEnergyConsumptionSet.getEBEnergyConsumption),
    path('existingBuildingEmissions/', views.ExistingBuildingEmissionsSet.existingBuildingEmissions),
    path('existingBuildingEmissions/<str:type>/<str:zone>/', views.ExistingBuildingEmissionsSet.updateEBEmissions),
    path('existingBuildingEmissions/<str:type>/<str:zone>/', views.ExistingBuildingEmissionsSet.getEBEmissions),
    path('newBuildingDemandDispersions/', views.NewBuildingDemandDispersionsSet.newBuildingDemandDispersions),
    path('newBuildingDemandDispersions/<str:type>/<str:zone>/', views.NewBuildingDemandDispersionsSet.updateNBDemandDispersions),
    path('newBuildingDemandDispersions/<str:type>/<str:zone>/', views.NewBuildingDemandDispersionsSet.getNBDemandDispersions),
    path('newBuildingEnergyAndEmissionsDispersions/', views.NewBuildingEnergyAndEmissionsDispersionsSet.newBuildingEnergyAndEmissionsDispersions),
    path('newBuildingEnergyAndEmissionsDispersions/<str:type>/<str:zone>/', views.NewBuildingEnergyAndEmissionsDispersionsSet.updateNBEnergyAndEmissionsDispersions),
    path('newBuildingEnergyAndEmissionsDispersions/<str:type>/<str:zone>/', views.NewBuildingEnergyAndEmissionsDispersionsSet.getNBEnergyAndEmissionsDispersions),
    path('existingBuildingDemandDispersions/', views.ExistingBuildingDemandDispersionsSet.existingBuildingDemandDispersions),
    path('existingBuildingDemandDispersions/<str:type>/<str:zone>/', views.ExistingBuildingDemandDispersionsSet.updateEBDemandDispersions),
    path('existingBuildingDemandDispersions/<str:type>/<str:zone>/', views.ExistingBuildingDemandDispersionsSet.getEBDemandDispersions),
    path('existingBuildingEnergyAndEmissionsDispersions/', views.ExistingBuildingEnergyAndEmissionsDispersionsSet.existingBuildingEnergyAndEmissionsDispersions),
    path('existingBuildingEnergyAndEmissionsDispersions/<str:type>/<str:zone>/', views.ExistingBuildingEnergyAndEmissionsDispersionsSet.updateEBEnergyAndEmissionsDispersions),
    path('existingBuildingEnergyAndEmissionsDispersions/<str:type>/<str:zone>/', views.ExistingBuildingEnergyAndEmissionsDispersionsSet.getEBEnergyAndEmissionsDispersions),
    path('buildingValues/', views.BuildingValuesSet.BuildingValue),
    path('buildingValues/<str:antiquity>/<str:value_type>/<str:indicator>/<str:building_type>/<str:climatic_zone>/', views.BuildingValuesSet.ModifyBuildingValues),
    path('softwareValues/', views.SoftwareValuesSet.SoftwareValue),
    path('softwareValues/<str:part_type>/<str:name>/', views.SoftwareValuesSet.ModifySoftwareValues),
    path('classificationData/', views.ClassificationDataSet.createClassification),
    path('classificationData/<str:number_metrics>/<str:classification>/', views.ClassificationDataSet.updateClassification),
    path('classificationDataC/<str:number_metrics>/<float:C>/', views.ClassificationDataSet.getClassificationC),
    path('classificationDataC1C2/<str:number_metrics>/<float:C1>/<float:C2>/', views.ClassificationDataSet.getClassificationC1C2),
    path('calculationData/', views.CalculationDataSet.createCalculationData),
    path('buildingCalculationData/<str:object>/<str:antiquity>/<str:value_type>/<str:indicator>/<str:object_type>/<str:climatic_zone>/<str:zone>/', views.CalculationDataSet.ModifyBuildingData),
    path('buildingMaximumData/<str:object>/<str:antiquity>/<str:value_type>/<str:indicator>/<str:object_type>/<str:climatic_zone>/<str:zone>/<str:classification>/', views.CalculationDataSet.getBuildingMaximumValue),
    path('softwareCalculationData/<str:object>/<str:object_type>/<str:value_type>/', views.CalculationDataSet.ModifySoftwareData),
    path('cpus/<str:object_type>/', views.CalculationDataSet.getCPUs),
    path('user/', views.UserViewSet.createUser),
    path('user/<str:email>', views.UserViewSet.modifyUser),
    path('user/<str:email>/folder', views.FileViewSet.getFiles),
    path('folder/', views.FileViewSet.createFile),
    path('folder/<int:id>', views.FileViewSet.modifyFile),
    path('folder/<str:email>/calcul', views.CalculViewSet.getCalculs),
    path('calcul/', views.CalculViewSet.createCalcul),
    path('calcul/<int:id>', views.CalculViewSet.modifyCalcul),   
]