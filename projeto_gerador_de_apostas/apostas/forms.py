from django import forms

class Aposta(forms.Form):
    quant = forms.IntegerField()