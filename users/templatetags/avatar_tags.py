from django import template

register = template.Library()


@register.filter
def filtrar_avatars_premium(self, user):
    """
    Funcion para filtrar los avatars de los usuarios premium
    """
    return self.filter(nivel__lte=user.nivel)