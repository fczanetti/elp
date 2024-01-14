from django.contrib import admin
from engplat.modulos.models import Modulo
from ordered_model.admin import OrderedModelAdmin


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ['titulo', 'slug', 'publico', 'order', 'move_up_down_links']
    prepopulated_fields = {'slug': ['titulo']}
    ordering = ('order',)
