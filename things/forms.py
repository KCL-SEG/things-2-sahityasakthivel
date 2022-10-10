"""Forms of the project."""
from django import forms
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = 'Name')
    description = forms.CharField(widget = forms.Textarea)
    quantity = forms.CharField(widget = forms.NumberInput)
