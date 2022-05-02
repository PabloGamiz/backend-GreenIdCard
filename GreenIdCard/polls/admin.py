from django.contrib import admin
from .models import (ClassificationData, ClassificationResidentialBuilding, ClassificationNotResidentialBuilding, NewBuildingDemand, NewBuildingEnergyConsume, NewBuildingEmissions, ExistingBuildingDemand, ExistingBuildingEnergyConsume, ExistingBuildingEmissions, NewBuldingDemandDispersions, NewBuldingEnergyAndEmissionsDispersions, ExistingBuldingDemandDispersions, ExistingBuldingEnergyAndEmissionsDispersions, ObjectData,User,File,Calcul)


# Register your models here.

admin.site.register(ClassificationResidentialBuilding)
admin.site.register(ClassificationNotResidentialBuilding)
admin.site.register(NewBuildingDemand)
admin.site.register(NewBuildingEnergyConsume)
admin.site.register(NewBuildingEmissions)
admin.site.register(ExistingBuildingDemand)
admin.site.register(ExistingBuildingEnergyConsume)
admin.site.register(ExistingBuildingEmissions)
admin.site.register(NewBuldingDemandDispersions)
admin.site.register(NewBuldingEnergyAndEmissionsDispersions)
admin.site.register(ExistingBuldingDemandDispersions)
admin.site.register(ExistingBuldingEnergyAndEmissionsDispersions)
admin.site.register(User)
admin.site.register(File)
admin.site.register(Calcul)
admin.site.register(ObjectData)
admin.site.register(ClassificationData)
