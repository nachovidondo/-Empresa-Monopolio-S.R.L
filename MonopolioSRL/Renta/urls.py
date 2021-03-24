
from django.urls import path
from .views import EditarReserva, EliminarReserva, OficinaListado,OficinaDetalle,CrearReserva,OficinaReservas

urlpatterns = [
    path('listado_oficina/',OficinaListado.as_view(),name ="listado_oficina"),
    path('detalle_oficina/<int:pk>/',OficinaDetalle.as_view(),name ="detalle_oficina"),
    path('crear_reserva/',CrearReserva.as_view(),name = "crear_reserva"),
    path('eliminar_reserva/<int:pk>/',EliminarReserva.as_view(),name ="eliminar_reserva"),
    path('editar_reserva/<int:pk>',EditarReserva.as_view(),name ="editar_reserva"),
    path('oficina_reserva/',OficinaReservas.as_view(),name ="oficina_reserva")
 

   
]
