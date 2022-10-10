"""Forms of the project."""
from django import forms
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 35)
    description = forms.CharField(maxlength= 120 empty_value = False,widget = forms.Textarea)
    quantity = forms.IntegerField(min_value = 0, max_value = 50,widget = forms.NumberInput)
