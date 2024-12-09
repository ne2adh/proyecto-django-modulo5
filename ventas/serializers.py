from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Venta
from .models import Cliente, Producto, Venta, Detalle

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()

    class Meta:
        model = Venta
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    venta = VentaSerializer()
    producto = ProductoSerializer()

    class Meta:
        model = Detalle
        fields = '__all__'

class VentaListCreateAPIView(ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer