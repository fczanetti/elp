from engplat.modulos.models import Modulo


def listar_modulos_ordenados():
    """
    Esta função deve buscar os módulos no banco de dados e listá-los de forma ordenada, do básico ao avançado.
    :return: Lista de módulos ordenada do básico ao avançado.
    """
    modulos = Modulo.objects.order_by('order').all()
    return modulos
