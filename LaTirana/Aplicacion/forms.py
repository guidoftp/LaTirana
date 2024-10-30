from django import forms
from Aplicacion.models import Libro
class FormLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'