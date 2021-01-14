from django import forms 


class ProductForm(forms.Form):
    item1 = forms.CharField(label= 'Item Name', max_length = 120)
    item2 = forms.DecimalField(label ='Zip Code', max_value = 2, max_digits= 100)
    