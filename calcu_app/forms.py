from django import forms

class SetupForm(forms.Form):
    nx = forms.IntegerField(label='nx')
    xmax = forms.IntegerField(label='xmax')
    c = forms.FloatField(label='c')
    alpha = forms.FloatField(label='alpha')
