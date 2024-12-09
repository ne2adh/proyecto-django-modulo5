from django import forms
from .models import Cliente, Producto, Venta, Detalle

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'


class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'