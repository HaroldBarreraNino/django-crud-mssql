# Generated by Django 4.2.2 on 2023-06-22 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renovables', '0004_alter_monto_pid_mmusd_proyecto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monto_pid_mmusd',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='renovables.proyectorenovable', to_field='nombre_del_proyecto'),
        ),
        migrations.AlterField(
            model_name='mw_incorporadas_por_ano',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='renovables.proyectorenovable', to_field='nombre_del_proyecto'),
        ),
        migrations.AlterField(
            model_name='proyectorenovable',
            name='nombre_del_proyecto',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]