from django import forms
from .models import Cifra_Clave

class CifraClaveForm(forms.ModelForm):

    Area = forms.ChoiceField(choices=[('Gas y GLP', 'Gas y GLP'), ('Portafolio de Gas, Inversiones y Actividad Upstream', 'Portafolio de Gas, Inversiones y Actividad Upstream'), ('Energéticos sociales', 'Energéticos sociales'), ('Energías Renovables', 'Energías Renovables'), ('Gestión Energética', 'Gestión Energética'), ('Hidrógeno', 'Hidrógeno'), ('CCUS', 'CCUS'), ('Movilidad sostenible', 'Movilidad sostenible'), ('Descarbonización', 'Descarbonización'), ('Micro LNG', 'Micro LNG'), ('Offshore', 'Offshore'), ('Portafolio Gas', 'Portafolio Gas'), ('Financieros', 'Financieros'), ('Hidrocarburos', 'Hidrocarburos'), ('Dimensión Ambiental', 'Dimensión Ambiental'), ('Dimensión Social', 'Dimensión Social'), ('Transmisión y vías', 'Transmisión y vías')])

    class Meta:
        model = Cifra_Clave
        fields = ['titulo', 'descripcion', 'Area']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }