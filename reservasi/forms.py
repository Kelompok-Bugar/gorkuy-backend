from django import forms

from database.models import Reservasi,Lapangan

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    reserve_date = forms.DateField(widget=DateInput)
    
class ReservasiForm(forms.ModelForm):
    jadwal = forms.MultipleChoiceField()
    class Meta:
        model = Reservasi
        fields = ['jadwal']
        widgets = {'jadwal':forms.CheckboxSelectMultiple}
        
    
	
