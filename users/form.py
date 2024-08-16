from django import forms
from .models import Persona

class Personaform(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '--all--'

