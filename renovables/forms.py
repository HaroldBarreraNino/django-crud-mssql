from django import forms
from .models import ProyectoRenovable
from .models import Monto_PID_MMUSD
from .models import MW_Incorporadas_por_ano

class ProyectoRenovableForm(forms.ModelForm):
    tecnologia = forms.ChoiceField(choices=[('Biomasa', 'Biomasa'), ('Eolico', 'Eolico'), ('Geotermia', 'Geotermia'), ('Hidraulica', 'Hidraulica'), ('Solar Fotovoltaica', 'Solar Fotovoltaica')])
    estado = forms.ChoiceField(choices=[('Construccion', 'Construccion'), ('Maduracion', 'Maduracion'), ('Operativo', 'Operativo')])
    tipo = forms.ChoiceField(choices=[('En Desarrollo', 'En Desarrollo'), ('Operativo', 'Operativo')])
    esquema_de_negocio = forms.ChoiceField(choices=[('Compra ENR', 'Compra ENR'), ('EDP', 'EDP'), ('Partnership', 'Partnership'), ('PPA', 'PPA')])
    ecopetrol_filial = forms.ChoiceField(choices=[('Ecopetrol', 'Ecopetrol'), ('Filial', 'Filial')])
    vicep_filial = forms.ChoiceField(choices=[('CENIT', 'CENIT'), ('GEE', 'GEE'), ('OCENSA', 'OCENSA'), ('ODC', 'ODC'), ('VAO', 'VAO'), ('VFS', 'VFS'), ('VPI', 'VPI'), ('VRC', 'VRC'), ('VRO', 'VRO'), ('VRP', 'VRP'), ('VSE', 'VSE')])
    riesgo_materializacion = forms.ChoiceField(choices=[('No', 'No'), ('Operativo', 'Operativo'), ('Si', 'Si')])
    
    class Meta:
        model = ProyectoRenovable
        fields = ['nombre_del_proyecto', 'tecnologia', 'estado', 'tipo', 'esquema_de_negocio', 'departamento', 'ecopetrol_filial', 'vicep_filial', 'activo', 'capacidad_instalada_MW_MWp_DC', 'reduccion_co2_ktCO2_año', 'inversion_ecopetrol', 'riesgo_materializacion', 'observaciones', 'lider_iniciativa']
        widgets = {
            'nombre_del_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_instalada_MW_MWp_DC': forms.NumberInput(attrs={'class': 'form-control'}),
            'reduccion_co2_ktCO2_año': forms.NumberInput(attrs={'class': 'form-control'}),
            'inversion_ecopetrol': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'lider_iniciativa': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MontoMMUSDForm(forms.ModelForm):
    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoRenovable.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    class Meta:
        model = Monto_PID_MMUSD
        fields = ['proyecto', 'año', 'monto']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MWIncorporadaForm(forms.ModelForm):
    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoRenovable.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    class Meta:
        model = MW_Incorporadas_por_ano
        fields = ['proyecto', 'año', 'montomw']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'montomw': forms.NumberInput(attrs={'class': 'form-control'}),
        }