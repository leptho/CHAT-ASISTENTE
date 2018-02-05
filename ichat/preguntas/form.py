from django import forms
from preguntas.models import Pregunta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = '__all__'
