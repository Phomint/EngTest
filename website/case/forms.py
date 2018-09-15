from django import forms
from .models import Contato

class ContatoModelForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields =['nome','celular','cargo','empresa','email',]

    def clean(self):
        cleaned_data = super(ContatoModelForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        celular = cleaned_data.get('celular')
        if not nome and not email:
            raise forms.ValidationError('You have to write something!')
