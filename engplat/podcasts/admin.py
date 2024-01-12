from django.contrib import admin
from engplat.podcasts.models import Podcast
# from ordered_model.admin import OrderedModelAdmin


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'data_gravacao', 'plat_id']
    prepopulated_fields = {'slug': ['titulo']}
    ordering = ['-data_gravacao']
