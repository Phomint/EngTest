from django import forms
from .models import Contato

class ContatoModelForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Nome do contato'}))

    celular = forms.CharField(help_text='Incluindo código do pais, exemplo +55011',  widget=forms.TextInput(
            attrs={'placeholder': 'Número do celular'}))

    cargo = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Cargo ou profissão'}))

    empresa = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Empresa em que trabalha'}))

    email = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Email completo'}))

    class Meta:
        model = Contato
        fields =['nome','celular','cargo','empresa','email',]

    def clean(self):
        cleaned_data = super(ContatoModelForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        celular = cleaned_data.get('celular')
        if not nome and not email:
            raise forms.ValidationError('Ops preencha os campos obrigatórios!')
