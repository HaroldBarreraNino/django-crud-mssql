from django.db import models

# Create your models here.
class ProyectoRenovable(models.Model):
    tecnologia = models.CharField(max_length=100)
    nombre_del_proyecto = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    esquema_de_negocio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    ecopetrol_filial = models.CharField(max_length=100)
    vicep_filial = models.CharField(max_length=100)
    activo = models.CharField(max_length=100)
    capacidad_instalada_MW_MWp_DC = models.FloatField(default=0)
    reduccion_co2_ktCO2_año = models.FloatField(default=0)
    inversion_ecopetrol = models.FloatField(default=0)
    riesgo_materializacion = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
    lider_iniciativa = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre_del_proyecto

class Monto_PID_MMUSD(models.Model):
    proyecto = models.ForeignKey(ProyectoRenovable, on_delete=models.PROTECT, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    monto = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.proyecto)
    
class MW_Incorporadas_por_ano(models.Model):
    proyecto = models.ForeignKey(ProyectoRenovable, on_delete=models.PROTECT, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    montomw = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.proyecto)