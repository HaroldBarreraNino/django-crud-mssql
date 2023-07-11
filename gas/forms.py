from django import forms
from .models import ProyectoGas
from .models import Inversiones_MUSD
from .models import Prod_Inc
from .models import WO
from .models import Pozos


class ProyectoGasForm(forms.ModelForm):

    escenario = forms.ChoiceField(
        choices=[('Resiliencia', 'Resiliencia'), ('Base', 'Base')])
    categoria = forms.ChoiceField(
        choices=[('ES', 'ES'), ('ICO', 'ICO'), ('NN', 'NN'), ('ON', 'ON'), ('OPT', 'OPT')])
    seguimiento = forms.ChoiceField(choices=[('Si', 'Si'), ('No', 'No')])
    recobro = forms.ChoiceField(choices=[(
        'Primario', 'Primario'), ('Secundario', 'Secundario'), ('Terciario', 'Terciario')])

    riesgo = forms.CharField(required=False)
    dimension = forms.CharField(required=False)
    proxima_toma_de_decision = forms.DateField(required=False)
    palanca_tecnologica = forms.CharField(required=False)
    capex_transicion = forms.IntegerField(required=False)

    class Meta:
        model = ProyectoGas
        fields = ['matricula_digital', 'nombre_del_proyecto', 'escenario', 'empresa', 'segmento', 'subsegmento', 'unidad_de_negocios_regional', 'gerencia', 'activo', 'departamento', 'categoria', 'subcategoria', 'fase_actual', 'riesgo', 'dimension', 'ejecutor', 'variante', 'proxima_toma_de_decision', 'fecha_fid', 'gas', 'seguimiento',
                  'palanca_tecnologica', 'cuenca_venture', 'hidrocarburo', 'recobro', 'capex_transicion', 'vpn_musd', 'e_vpn_musd', 'efi_veces', 'tir', 'parback_meses', 'be_crudo', 'be_gas', 'capex_unitario', 'first_oil_gas', 'volumenes_1p', 'volumenes_2p', 'volumenes_3p', 'recursos_contigentes', 'rec_desc_delimitar_verificar', 'recursos_prospectivos']
        widgets = {
            'matricula_digital': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_del_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'segmento': forms.TextInput(attrs={'class': 'form-control'}),
            'subsegmento': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_de_negocios_regional': forms.TextInput(attrs={'class': 'form-control'}),
            'gerencia': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'fase_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'riesgo': forms.TextInput(attrs={'class': 'form-control'}),
            'dimesion': forms.TextInput(attrs={'class': 'form-control'}),
            'ejecutor': forms.TextInput(attrs={'class': 'form-control'}),
            'variante': forms.TextInput(attrs={'class': 'form-control'}),
            'proxima_toma_de_decision': forms.DateInput(format='%d/%m/%Y'),
            'fecha_fid': forms.DateInput(format='%d/%m/%Y'),
            'gas': forms.NumberInput(attrs={'class': 'form-control'}),
            'palanca_tecnologica': forms.TextInput(attrs={'class': 'form-control'}),
            'cuenca_venture': forms.TextInput(attrs={'class': 'form-control'}),
            'hidrocarburo': forms.TextInput(attrs={'class': 'form-control'}),
            'capex_transicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'vpn_musd': forms.NumberInput(attrs={'class': 'form-control'}),
            'e_vpn_musd': forms.NumberInput(attrs={'class': 'form-control'}),
            'efi_veces': forms.NumberInput(attrs={'class': 'form-control'}),
            'tir': forms.NumberInput(attrs={'class': 'form-control'}),
            'parback_meses': forms.NumberInput(attrs={'class': 'form-control'}),
            'be_crudo': forms.NumberInput(attrs={'class': 'form-control'}),
            'be_gas': forms.NumberInput(attrs={'class': 'form-control'}),
            'capex_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_oil_gas': forms.NumberInput(attrs={'class': 'form-control'}),
            'volumenes_1p': forms.NumberInput(attrs={'class': 'form-control'}),
            'volumenes_2p': forms.NumberInput(attrs={'class': 'form-control'}),
            'volumenes_3p': forms.NumberInput(attrs={'class': 'form-control'}),
            'recursos_contigentes': forms.NumberInput(attrs={'class': 'form-control'}),
            'rec_desc_delimitar_verificar': forms.NumberInput(attrs={'class': 'form-control'}),
            'receursos_prospectivos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class InversionesMUSDForm(forms.ModelForm):

    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoGas.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    mes = forms.ChoiceField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), (
        'Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')])

    class Meta:
        model = Inversiones_MUSD
        fields = ['proyecto', 'mes', 'año', 'monto']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProdIncForm(forms.ModelForm):

    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoGas.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    class Meta:
        model = Prod_Inc
        fields = ['proyecto', 'año', 'valor']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PozosForm(forms.ModelForm):

    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoGas.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    class Meta:
        model = Pozos
        fields = ['proyecto', 'año', 'cantidad']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class WOForm(forms.ModelForm):

    def clean_proyecto(self):
        proyecto = self.cleaned_data.get('proyecto')
        if not ProyectoGas.objects.filter(nombre_del_proyecto=proyecto).exists():
            raise forms.ValidationError("El proyecto que digito no existe.")
        return proyecto

    class Meta:
        model = WO
        fields = ['proyecto', 'año', 'valor']
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
