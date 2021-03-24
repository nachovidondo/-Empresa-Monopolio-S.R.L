
from .models import Reserva,Oficina
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import FormularioCrearReserva
from django.urls.base import reverse_lazy
# Create your views here.

#CRUD OFICINA
class OficinaListado(ListView):
    model = Oficina
    template_name = 'listado_oficina.html'
    context_object_name = "oficinas"
    
class OficinaDetalle(DetailView):
    model = Oficina
    template_name = 'detalle_oficina.html'
    context_object_name = "oficina"
    
class OficinaReservas(ListView):
    
    model = Reserva
    template_name ='oficina_reservas.html'
    context_object_name = "obj"
    # PASO DE PARAMETROS POR QUERYSTRINGS
    def get_queryset(self):
        qs= Reserva.objects.order_by('-id')[:20]
        oficina_id = self.request.GET.get('lang')
        if oficina_id:
            qs = qs.filter(oficina__id = oficina_id)
            
        return qs    
    
    

# CRUD RESERVAS
class CrearReserva(CreateView):
    model = Reserva
    form_class =FormularioCrearReserva
    template_name = 'crear_reserva.html'
    success_url = reverse_lazy('listado_oficina')
    
class EliminarReserva(DeleteView):
    model = Reserva
    success_url = reverse_lazy('listado_oficina')
  


class EditarReserva(UpdateView):
    model = Reserva
    template_name ='editar_reserva.html'
    form_class = FormularioCrearReserva
    success_url = reverse_lazy('listado_oficina')