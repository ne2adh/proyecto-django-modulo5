from django.urls import path, include
from .serializers import VentaListCreateAPIView, VentaRetrieveUpdateDestroyAPIView
from rest_framework.routers import DefaultRouter

from . import views
from .views import ClienteViewSet, ProductoViewSet, VentaViewSet, DetalleViewSet, total_ventas

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalles', DetalleViewSet)

app_name = 'ventas'

urlpatterns = [
    #path('', include(router.urls)),
    path('total_ventas/', total_ventas, name='total_ventas'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', views.producto_edit, name='producto_edit'),
    path('productos/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),
    path('ventas/', views.venta_list, name='venta_list'),
    path('ventas/nuevo/', views.venta_create, name='venta_create'),
    path('ventas/editar/<int:pk>/', views.venta_edit, name='venta_edit'),
    path('ventas/eliminar/<int:pk>/', views.venta_delete, name='venta_delete'),
    path('detalles/', views.detalle_list, name='detalle_list'),
    path('detalles/nuevo/', views.detalle_create, name='detalle_create'),
    path('detalles/editar/<int:pk>/', views.detalle_edit, name='detalle_edit'),
    path('detalles/eliminar/<int:pk>/', views.detalle_delete, name='detalle_delete'),

    path('ventas/', VentaListCreateAPIView.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', VentaRetrieveUpdateDestroyAPIView.as_view(), name='venta-detail'),
]
