from engplat.modulos.models import Modulo


def listar_modulos_ordenados():
    """
    Esta função deve buscar os módulos no banco de dados e listá-los de forma ordenada, do básico ao avançado.
    :return: Lista de módulos ordenada do básico ao avançado.
    """
    modulos = Modulo.objects.order_by('order').all()
    return modulos


def buscar_modulo(slug):
    """
    Busca o módulo no banco de dados através da slug.
    :param slug: Parâmetro para localizar o módulo.
    :return: Objeto Modulo.
    """
    modulo = Modulo.objects.get(slug=slug)
    return modulo


def listar_aulas_de_modulo_ordenadas(modulo):
    """
    Lista as aulas de um módulo específico.
    :param modulo: Módulo do qual as aulas serão listadas.
    :return: Lista de aulas do módulo informado como parâmetro.
    """
    aulas = modulo.aula_set.order_by('order').all()
    return aulas
