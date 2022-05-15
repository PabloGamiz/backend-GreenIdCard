from django.db import models

# Create your models here.

class ClassificationResidentialBuilding(models.Model):
    calification = models.CharField(max_length=4, primary_key = True)
    min_C1 = models.DecimalField(decimal_places=3, max_digits=10, null=False)
    max_C1 = models.DecimalField(decimal_places=3, max_digits=10, null=False)
    min_C2 = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    max_C2 = models.DecimalField(decimal_places=3, max_digits=10, null=True)

class ClassificationNotResidentialBuilding(models.Model):
    calification = models.CharField(max_length=4, primary_key = True)
    min_C = models.FloatField(null=False)
    max_C = models.FloatField(null=False)

    def __str__(self):
        return self.calification + " " + self.min_C + " " + self.max_C

class NewBuildingDemand(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration
    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class NewBuildingEnergyConsume(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()
    ACS = models.FloatField()

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration + " " + self.ACS
    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class NewBuildingEmissions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()
    ACS = models.FloatField()

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration + " " + self.ACS

    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class ExistingBuildingDemand(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()

    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class ExistingBuildingEnergyConsume(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()
    ACS = models.FloatField()

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration + " " + self.ACS

    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class ExistingBuildingEmissions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    heating = models.FloatField()
    refrigeration = models.FloatField()
    ACS = models.FloatField()

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration + " " + self.ACS

    def __str__(self):
        return self.building_type + " " + self.climatic_zone + " " + self.heating + " " + self.refrigeration + " " + self.ACS
    class Meta:
        unique_together = [["building_type", "climatic_zone"]]

class NewBuldingDemandDispersions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    dispersion = models.FloatField(null=True)

    unique_together = [["building_type", "climatic_zone"]]

class NewBuldingEnergyAndEmissionsDispersions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    dispersion = models.FloatField(null=True)

    unique_together = [["building_type", "climatic_zone"]]

class ExistingBuldingDemandDispersions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    dispersion = models.FloatField(null=True)

    unique_together = [["building_type", "climatic_zone"]]

class ExistingBuldingEnergyAndEmissionsDispersions(models.Model):
    building_type = models.IntegerField()
    climatic_zone = models.CharField(max_length=4)
    dispersion = models.FloatField(null=True)

    unique_together = [["building_type", "climatic_zone"]]

class SystemUser(models.Model):
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='name')
    surname = models.CharField(max_length=100, default='surname')
    password = models.CharField(max_length=100, default='password')
    

class File(models.Model):
    name = models.CharField(max_length=100, default='name')
    description = models.CharField(max_length=100)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)

class Calcul(models.Model):
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    value11 = models.CharField(max_length=100, default='0.0')
    calification11 =  models.CharField(max_length=100, default='A')
    value12 = models.CharField(max_length=100, default='0.0')
    calification12 =  models.CharField(max_length=100, default='A')
    value13 = models.CharField(max_length=100, default='0.0')
    calification13 =  models.CharField(max_length=100, default='A')
    value21 = models.CharField(max_length=100, null=True)
    calification21 =  models.CharField(max_length=100, null=True)
    value22 = models.CharField(max_length=100, null=True)
    calification22 =  models.CharField(max_length=100, null=True)
    value23 = models.CharField(max_length=100, null=True)
    calification23 =  models.CharField(max_length=100, null=True)
    value31 = models.CharField(max_length=100, null=True)
    calification31 =  models.CharField(max_length=100, null=True)
    value32 = models.CharField(max_length=100, null=True)
    calification32 =  models.CharField(max_length=100, null=True)
    value33 = models.CharField(max_length=100, null=True)
    calification33 =  models.CharField(max_length=100, null=True)
    

class BuildingValues(models.Model):
    antiquity = models.CharField(max_length=100)    # nou, existent
    value_type = models.CharField(max_length=100)   # mean, dispersion
    indicator = models.CharField(max_length=100)    # demanda, consum d'energia, emissions
    object_type = models.CharField(max_length=100) # unifamiliar, bloc
    climatic_zone = models.CharField(max_length=4)  # A1, A2, D4...
    value1 = models.FloatField()
    value2 = models.FloatField()
    value3 = models.FloatField()


class SoftwareValues(models.Model):
    part_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    core_number = models.IntegerField()
    consumption = models.FloatField()

class ClassificationData(models.Model):
    calification = models.CharField(max_length=4)
    number_metrics = models.CharField(max_length=2, default=1)
    min_C1 = models.DecimalField(decimal_places=2, max_digits=10)
    max_C1 = models.DecimalField(decimal_places=2, max_digits=10)
    min_C2 = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    max_C2 = models.DecimalField(decimal_places=2, max_digits=10, null=True)


class ObjectData(models.Model):
    object = models.CharField(max_length=100)  #building, sistema software
    object_type = models.CharField(max_length=100) # unifamiliar, bloc
    value_type = models.CharField(max_length=100)   # mean, dispersion
    indicator = models.CharField(max_length=100, null=True)    # demanda, consum d'energia, emissions
    antiquity = models.CharField(max_length=100, null=True)    # nou, existent
    climatic_zone = models.CharField(max_length=4, null=True)  # A1, A2, D4...
    value1 = models.DecimalField(decimal_places=2, max_digits=100)
    value2 = models.DecimalField(decimal_places=2, max_digits=100, null = True)
    value3 = models.DecimalField(decimal_places=2, max_digits=100, null=True)
