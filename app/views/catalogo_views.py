# app/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from app.forms import CatalogoForm
from app.models import Catalogo



class CatalogoBaseView:
    """Clase base con configuración común"""
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'app/catalogo/form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.view_type  # Definido en cada clase hija
        context['titulo'] = self.get_title()
        return context

class CatalogoCreateView(CatalogoBaseView, CreateView):
    success_url = reverse_lazy('lista_catalogos')
    view_type = 'crear'
    
    def get_title(self):
        return 'Crear Nuevo Producto'

class CatalogoUpdateView(CatalogoBaseView, UpdateView):
    success_url = reverse_lazy('lista_catalogos')
    view_type = 'editar'
    
    def get_title(self):
        return f'Editar: {self.object.nombre}'

class CatalogoDetailView(CatalogoBaseView, DetailView):
    view_type = 'ver'
    
    def get_title(self):
        return f'Detalles: {self.object.nombre}'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CatalogoForm(instance=self.object)
        return context






class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'app/catalogo/lista.html'
    context_object_name = 'catalogos'







class CatalogoDeleteView(DeleteView):
    model = Catalogo
    template_name = 'app/catalogo_confirmar_eliminar.html'
    success_url = reverse_lazy('lista_catalogos')