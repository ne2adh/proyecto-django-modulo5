from django.core.exceptions import ValidationError

def validate_precio_unitario(value):
    if value <= 0:
        raise ValidationError("El valor del precio unitario debe ser mayor a 0.")

def validate_cantidad(value):
    if value <= 0:
        raise ValidationError("El valor de la cantidad debe ser mayor a 0.")