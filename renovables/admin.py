from django.contrib import admin
from .models import ProyectoRenovable
from .models import Monto_PID_MMUSD
from .models import MW_Incorporadas_por_ano

# Register your models here.
admin.site.register(ProyectoRenovable)
admin.site.register(Monto_PID_MMUSD)
admin.site.register(MW_Incorporadas_por_ano)