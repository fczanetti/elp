from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe_modulo', args=(self.slug,))


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT)
    plat_id = models.CharField(max_length=32)
    order_with_respect_to = 'modulo'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe_aula', args=(self.slug,))
