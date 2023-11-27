from django import forms

class Add_produ(forms.Form):
    nombre = forms.CharField(max_length=100)
    stonk = forms.IntegerField()
    