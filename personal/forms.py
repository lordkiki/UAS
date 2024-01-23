from django import forms
from personal.models import Tbcars

class TbcarsForm(forms.ModelForm):
    class Meta:
        model = Tbcars
        fields = ['carname', 'carbrand', 'carmodel', 'carprice']
        widgets = {'carname': forms.TextInput(attrs={'class':'form-control'}),
                   'carbrand': forms.TextInput(attrs={'class':'form-control'}),
                   'carmodel': forms.TextInput(attrs={'class':'form-control'}),
                   'carprice': forms.TextInput(attrs={'class':'form-control'}),
                   }