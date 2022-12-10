from django import forms
from django.forms import fields
from django.forms.widgets import Input, Textarea
from database.models import *


class RescheduleForm(forms.ModelForm):
    jadwal = forms.MultipleChoiceField()
    class Meta:
        model = Reservasi
        fields = ['jadwal']
        widgets = {'jadwal':forms.CheckboxSelectMultiple}
        
    
	
