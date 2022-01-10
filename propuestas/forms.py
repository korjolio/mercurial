from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from propuestas.models import Cliente

class DropdownClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('tipo_pers',)
        widgets = {
            'tipo_pers': forms.Select(choices=Cliente.tipo_pers)
        }

