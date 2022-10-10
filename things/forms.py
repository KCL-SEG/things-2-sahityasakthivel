"""Forms of the project."""
from django import forms
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 35)
    description = forms.CharField(widget = forms.Textarea)
    quantity = forms.CharField(widget = forms.NumberInput(attrs={'min':0, 'max' : 50}))
