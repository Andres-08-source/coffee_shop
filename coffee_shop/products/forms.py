from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-lg p-2'})
    )
    description = forms.CharField(
        max_length=500,
        label="Descripción",
        widget=forms.Textarea(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-lg p-2'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Precio",
        widget=forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-lg p-2'})
    )
    avaliable = forms.BooleanField(
        initial=True,
        label="Disponible",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'mr-2'})
    )
    photo = forms.ImageField(
        label="Foto",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'mt-1 block w-full'})
    )

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            avaliable=self.cleaned_data["avaliable"],
            photo=self.cleaned_data["photo"]
        )
