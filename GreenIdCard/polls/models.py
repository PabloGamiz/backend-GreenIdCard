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

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class File(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Calcul(models.Model):
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    value = models.FloatField()
    calification = models.CharField(max_length=100)
    consumption = models.FloatField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)

class BuildingValues(models.Model):
    antiquity = models.CharField(max_length=100)    # nou, existent
    value_type = models.CharField(max_length=100)   # mean, dispersion
    indicator = models.CharField(max_length=100)    # dispersio, consum d'energia, emissions
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
    antiquity = models.CharField(max_length=100)    # nou, existent
    value_type = models.CharField(max_length=100)   # mean, dispersion
    indicator = models.CharField(max_length=100)    # demanda, consum d'energia, emissions
    object_type = models.CharField(max_length=100) # unifamiliar, bloc
    climatic_zone = models.CharField(max_length=4)  # A1, A2, D4...
    value1 = models.DecimalField(decimal_places=2, max_digits=100)
    value2 = models.DecimalField(decimal_places=2, max_digits=100)
    value3 = models.DecimalField(decimal_places=2, max_digits=100)
