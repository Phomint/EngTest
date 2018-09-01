from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length = 120, verbose_name='Nome')
    celular = models.IntegerField(verbose_name='Celular')
    cargo = models.CharField(max_length = 120, verbose_name='Cargo')
    empresa = models.CharField(max_length = 50, verbose_name='Empresa')
    email = models.EmailField(max_length = 120, verbose_name='Email')

    def get_absolute_url(self):
            return reverse("cliente:detail", kwargs={"id": self.id})
