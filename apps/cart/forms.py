from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label="数量",choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
	# quantity = forms.IntegerField(label='数量',required=True,min_value=1,widget=forms.NumberInput(attrs={"class":"int_number","value":"1"}))
	update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)