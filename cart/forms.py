from django import forms
from .models import CartItem

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class CartItemForm(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = ('item', 'time_desired')

        widgets = {'time_desired': DateTimeInput()}

