from django.db import models

class ClassificationData(models.Model):
    calification = models.CharField(max_length=4)
    number_metrics = models.CharField(max_length=2, default=1)
    min_C1 = models.DecimalField(decimal_places=2, max_digits=10, default = 0.0)
    max_C1 = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    min_C2 = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    max_C2 = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)

    class Meta:
        unique_together = [["calification", "number_metrics"]]


class ObjectData(models.Model):
    object = models.CharField(max_length=100)  #building, sistema software
    object_type = models.CharField(max_length=100) # unifamiliar, bloc
    value_type = models.CharField(max_length=100)   # mean, dispersion
    indicator = models.CharField(max_length=100, default='default')    # demanda, consum d'energia, emissions
    antiquity = models.CharField(max_length=100, default='default')    # nou, existent
    zone = models.CharField(max_length=100, default='default') #España, Islas canarias
    climatic_zone = models.CharField(max_length=7, default='default')  # A1, A2, D4...
    classification = models.CharField(max_length=7, default= 'default')
    value1 = models.DecimalField(decimal_places=2, max_digits=100, default=0.0)
    value2 = models.DecimalField(decimal_places=2, max_digits=100, default=0.0)
    value3 = models.DecimalField(decimal_places=2, max_digits=100, default=0.0)

    class Meta:
        unique_together = [["object", "object_type", "value_type", "indicator", "antiquity", "zone", "climatic_zone"]]
