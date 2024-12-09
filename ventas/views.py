from django.shortcuts import render

# Create your views here.
from .models import Venta
from .serializers import VentaSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Producto, Venta, Detalle
from .forms import ClienteForm, ProductoForm, VentaForm, DetalleForm
from .serializers import ClienteSerializer, ProductoSerializer, VentaSerializer, DetalleSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer

@api_view(['GET'])
def total_ventas(request):
    total_ventas = Venta.objects.count()
    return Response({'total_ventas': total_ventas})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Venta, Detalle
from .forms import ClienteForm, ProductoForm, VentaForm, DetalleForm

# Vistas para Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form, 'cliente': cliente})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('ventas:cliente_list')

# Vistas para Producto
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:producto_list')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ventas:producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'producto': producto})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('ventas:producto_list')

# Vistas para Venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:venta_list')
    else:
        form = VentaForm()
    return render(request, 'venta_form.html', {'form': form})

def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas:venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta_form.html', {'form': form, 'venta': venta})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    venta.delete()
    return redirect('ventas:venta_list')

# Vistas para Detalle
def detalle_list(request):
    detalles = Detalle.objects.all()
    return render(request, 'detalle_list.html', {'detalles': detalles})

def detalle_create(request):
    if request.method == 'POST':
        form = DetalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:detalle_list')
    else:
        form = DetalleForm()
    return render(request, 'detalle_form.html', {'form': form})

def detalle_edit(request, pk):
    detalle = get_object_or_404(Detalle, pk=pk)
    if request.method == 'POST':
        form = DetalleForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('ventas:detalle_list')
    else:
        form = DetalleForm(instance=detalle)
    return render(request, 'detalle_form.html', {'form': form, 'detalle': detalle})

def detalle_delete(request, pk):
    detalle = get_object_or_404(Detalle, pk=pk)
    detalle.delete()
    return redirect('ventas:detalle_list')