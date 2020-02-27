from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int, widget=forms.Select(
            attrs={
                'style': 'background: none; padding: 2px',
            }))  # user can input quantity from 1 to 20, input is converted into int
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)  # false - adding to the existing, true - replace the existing with new; widget will hide this choice
