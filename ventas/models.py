from django.db import models
from .validators import validate_cantidad, validate_precio_unitario
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_precio_unitario])
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField()
    observacion = models.TextField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')

    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

class Detalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField(validators=[validate_cantidad])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_precio_unitario])

    def __str__(self):
        return f"Detalle {self.id} - {self.venta}"