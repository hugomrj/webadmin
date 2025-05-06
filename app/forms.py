# app/forms.py
from django import forms
from .models import Catalogo, Imagen

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'precio', 'edad', 'estado']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'estado': forms.Select(choices=Catalogo.ESTADO_CHOICES),
        }