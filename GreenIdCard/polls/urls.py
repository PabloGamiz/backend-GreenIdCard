from django.contrib import admin
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from . import views

from django.urls import path, register_converter

from . import converts, views

register_converter(converts.FloatUrlParameterConverter, 'float')


urlpatterns =[
    path('classificationData', views.ClassificationDataSet.createClassification),
    path('classificationData/<str:number_metrics>/<str:classification>', views.ClassificationDataSet.updateClassification),
    path('classificationDataC/<str:number_metrics>/<float:C>', views.ClassificationDataSet.getClassificationC),
    path('classificationDataC1C2/<str:number_metrics>/<float:C1>/<float:C2>', views.ClassificationDataSet.getClassificationC1C2),
    path('calculationData', views.CalculationDataSet.createCalculationData),
    path('buildingCalculationData/<str:object>/<str:antiquity>/<str:value_type>/<str:indicator>/<str:object_type>/<str:climatic_zone>/<str:zone>', views.CalculationDataSet.ModifyBuildingData),
    path('buildingMaximumData/<str:object>/<str:antiquity>/<str:value_type>/<str:indicator>/<str:object_type>/<str:climatic_zone>/<str:zone>/<str:classification>', views.CalculationDataSet.getBuildingMaximumValue),
    path('softwareCalculationData/<str:object>/<str:object_type>/<str:value_type>', views.CalculationDataSet.ModifySoftwareData),
    path('cpus/<str:object>/<str:object_type>', views.CalculationDataSet.getCPUs),
]