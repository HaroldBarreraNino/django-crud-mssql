# Generated by Django 4.2.2 on 2023-06-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renovables', '0005_alter_monto_pid_mmusd_proyecto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monto_pid_mmusd',
            name='año',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mw_incorporadas_por_ano',
            name='año',
            field=models.IntegerField(null=True),
        ),
    ]
