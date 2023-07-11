# Generated by Django 4.2.2 on 2023-06-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renovables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectorenovable',
            name='capacidad_instalada_MW_MWp_DC',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='proyectorenovable',
            name='inversion_ecopetrol',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='proyectorenovable',
            name='reduccion_co2_ktCO2_año',
            field=models.FloatField(default=0),
        ),
    ]
