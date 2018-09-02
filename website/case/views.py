from django.shortcuts import render, get_object_or_404
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
    queryset = Contato.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ContatoListView(ListView):
    template_name = 'contato/contato_list.html'
    queryset = Contato.objects.all()


class ContatoDetailView(DetailView):
    template_name = 'contato/contato_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Contato, id=id_)


class ContatoUpdateView(UpdateView):
    template_name = 'contato/contato_create.html'
    form_class = ContatoModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Contato, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ContatoDeleteView(DeleteView):
    template_name = 'contato/contato_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Contato, id=id_)

    def get_success_url(self):
        return reverse('contato:contato-list')
