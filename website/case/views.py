from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import ContatoModelForm
from .models import Contato
class ContatoCreateView(CreateView):
    template_name = 'contato/contato_create.html'
    form_class = ContatoModelForm
    model = Contato

class ContatoListView(ListView):
    template_name = 'contato/contato_list.html'
    model = Contato

class ContatoDetailView(DetailView):
    template_name = 'contato/contato_detail.html'
    model = Contato

class ContatoUpdateView(UpdateView):
    template_name = 'contato/contato_create.html'
    form_class = ContatoModelForm
    model = Contato

class ContatoDeleteView(DeleteView):
    template_name = 'contato/contato_delete.html'
    model = Contato
    def get_success_url(self):
        return reverse('contato:contato-list')
