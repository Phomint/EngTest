from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Contato(models.Model):
    nome = models.CharField(max_length = 120, verbose_name='Nome')
    celular = PhoneNumberField(verbose_name='Celular')
    cargo = models.CharField(max_length = 120, verbose_name='Cargo', blank='True')
    empresa = models.CharField(max_length = 50, verbose_name='Empresa', blank='True')
    email = models.EmailField(max_length = 120, verbose_name='Email', blank='True')

    def get_absolute_url(self):
        return reverse("contato:contato-detail", kwargs={"pk": self.id})
