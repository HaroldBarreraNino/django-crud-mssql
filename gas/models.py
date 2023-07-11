from django.db import models

# Create your models here.
class ProyectoGas(models.Model):
    matricula_digital = models.CharField(max_length=100, default='')
    nombre_del_proyecto = models.CharField(max_length=100, unique=True, default='')
    escenario = models.CharField(max_length=100, default='')
    empresa = models.CharField(max_length=100, default='')
    segmento = models.CharField(max_length=100, default='')
    subsegmento = models.CharField(max_length=100, default='')
    unidad_de_negocios_regional = models.CharField(max_length=100, default='')
    gerencia = models.CharField(max_length=100, default='')
    activo = models.CharField(max_length=100, default='')
    departamento = models.CharField(max_length=100, default='')
    categoria = models.CharField(max_length=100, default='')
    subcategoria = models.CharField(max_length=100, default='')
    fase_actual = models.CharField(max_length=100, default='')
    riesgo = models.CharField(max_length=100, default='')
    dimension = models.CharField(max_length=100, default='')
    ejecutor = models.CharField(max_length=100, default='')
    variante = models.CharField(max_length=100, default='')
    proxima_toma_de_decision = models.DateField(null=True)
    fecha_fid = models.DateField(null=True)
    gas = models.IntegerField(null=True)
    seguimiento = models.CharField(max_length=100, default='')
    palanca_tecnologica = models.CharField(max_length=100, default='')
    cuenca_venture = models.CharField(max_length=100, default='')
    hidrocarburo = models.CharField(max_length=100, default='')
    recobro = models.CharField(max_length=100, default='')
    capex_transicion = models.IntegerField(null=True)
    vpn_musd = models.IntegerField(null=True)
    e_vpn_musd = models.IntegerField(null=True)
    efi_veces = models.IntegerField(null=True)
    tir = models.IntegerField(null=True)
    parback_meses = models.IntegerField(null=True)
    be_crudo = models.IntegerField(null=True)
    be_gas = models.IntegerField(null=True)
    capex_unitario = models.IntegerField(null=True)
    first_oil_gas = models.IntegerField(null=True)
    volumenes_1p = models.IntegerField(null=True)
    volumenes_2p = models.IntegerField(null=True)
    volumenes_3p = models.IntegerField(null=True)
    recursos_contigentes = models.IntegerField(null=True)
    rec_desc_delimitar_verificar = models.IntegerField(null=True)
    recursos_prospectivos = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.nombre_del_proyecto
    
class Inversiones_MUSD(models.Model):
    proyecto = models.ForeignKey(ProyectoGas, on_delete=models.CASCADE, to_field='nombre_del_proyecto')
    mes = models.CharField(max_length=20, default='Enero')
    año = models.IntegerField(null=True)
    monto = models.FloatField(default=0)

class Operaciones(models.Model):
    proyecto = models.ForeignKey(ProyectoGas, on_delete=models.CASCADE, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    total = models.FloatField(default=0)
    contingencia = models.FloatField(default=0)
    capex = models.FloatField(default=0)

class Prod_Inc(models.Model):
    proyecto = models.ForeignKey(ProyectoGas, on_delete=models.CASCADE, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    valor = models.FloatField(default=0)

class Pozos(models.Model):
    proyecto = models.ForeignKey(ProyectoGas, on_delete=models.CASCADE, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    cantidad = models.IntegerField(null=0)

class WO(models.Model):
    proyecto = models.ForeignKey(ProyectoGas, on_delete=models.CASCADE, to_field='nombre_del_proyecto')
    año = models.IntegerField(null=True)
    valor = models.IntegerField(null=0)