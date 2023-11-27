from django import forms

class Add_prove(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=8)
    