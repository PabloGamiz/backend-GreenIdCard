# Generated by Django 4.0.3 on 2022-06-18 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuildingValues',
        ),
        migrations.DeleteModel(
            name='Calcul',
        ),
        migrations.DeleteModel(
            name='ClassificationNotResidentialBuilding',
        ),
        migrations.DeleteModel(
            name='ClassificationResidentialBuilding',
        ),
        migrations.DeleteModel(
            name='ExistingBuildingDemand',
        ),
        migrations.DeleteModel(
            name='ExistingBuildingEmissions',
        ),
        migrations.DeleteModel(
            name='ExistingBuildingEnergyConsume',
        ),
        migrations.DeleteModel(
            name='ExistingBuldingDemandDispersions',
        ),
        migrations.DeleteModel(
            name='ExistingBuldingEnergyAndEmissionsDispersions',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='NewBuildingDemand',
        ),
        migrations.DeleteModel(
            name='NewBuildingEmissions',
        ),
        migrations.DeleteModel(
            name='NewBuildingEnergyConsume',
        ),
        migrations.DeleteModel(
            name='NewBuldingDemandDispersions',
        ),
        migrations.DeleteModel(
            name='NewBuldingEnergyAndEmissionsDispersions',
        ),
        migrations.DeleteModel(
            name='SoftwareValues',
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]