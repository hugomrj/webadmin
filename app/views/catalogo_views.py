# app/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from app.forms import CatalogoForm
from app.models import Catalogo



class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'app/catalogo/lista.html'
    context_object_name = 'catalogos'





class CatalogoCreateView(CreateView):
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'app/catalogo_form.html'
    success_url = reverse_lazy('lista_catalogos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Catálogo'
        return context

class CatalogoUpdateView(UpdateView):
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'app/catalogo_form.html'
    success_url = reverse_lazy('lista_catalogos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Catálogo'
        return context

class CatalogoDeleteView(DeleteView):
    model = Catalogo
    template_name = 'app/catalogo_confirmar_eliminar.html'
    success_url = reverse_lazy('lista_catalogos')