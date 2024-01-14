from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    slug = models.SlugField(unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', args=(self.slug,))
