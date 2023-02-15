from django import forms

class JuegosFormulario(forms.Form):

    nombre = forms.CharField()
    categoria = forms.CharField()
    valoracion = forms.IntegerField()

class CategoriasFormulario(forms.Form):
    nombre = forms.CharField()

class LanzamientosFormulario(forms.Form):
    nombre = forms.CharField()
    categoria = forms.CharField()
    fecha_de_lanzamiento = forms.DateField()