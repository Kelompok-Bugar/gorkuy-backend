from django import forms
from django.forms import fields
from django.forms.widgets import Input, Textarea
from database.models import Reservasi,Lapangan


class ReservasiForm(forms.ModelForm):
    
    class Meta:
        model = Reservasi
        jadwal = forms.MultipleChoiceField(    
            widget  = forms.CheckboxSelectMultiple,
        )
    
	
