from django.db import models
from django.urls import reverse


class Podcast(models.Model):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    data_gravacao = models.DateField()
    plat_id = models.CharField(max_length=32)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('podcasts:detalhe', kwargs={'slug': self.slug})
