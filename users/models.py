""" Modelos de la app usuarios """
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class Avatar(models.Model):
    """ Clase que representa un avatar """
    nombre_imagen = models.CharField(max_length=20, blank=False)
    nombre_a_mostrar = models.CharField(max_length=20, blank=False)
    descripcion = models.TextField(max_length=50, blank=True)
    NIVELES = ((0, _('sin premium')),
               (1, _('premium basico')),
               (2, _('premium medio')),
               (3, _('premium avanzado')),
               )
    nivel = models.IntegerField(choices=NIVELES,
                                default=0)

    def __str__(self):
        return self.nombre_a_mostrar


class User(AbstractUser):
    """ Clase que sobreescribe el usuario que utiliza django por defecto,
    agregando algunos campos extra"""
    # Importo los paises de un .txt
    paises = []
    file1 = open('users/resources/paises.txt', 'r')
    count = 0
    for line in file1:
        count += 1
        paises.append((line.replace("\n", ""), line.replace("\n", "")))
    file1.close()
    biografia = models.TextField(max_length=500, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    intereses = models.CharField(max_length=100, blank=True)

    NIVELES = ((0, _('sin premium')),
               (1, _('premium basico')),
               (2, _('premium medio')),
               (3, _('premium avanzado')),
               )

    nivel = models.IntegerField(choices=NIVELES,
                                default=0)
    RANKINGS = ['sin ranking', 'bronce', 'plata', 'oro']

    pais = models.CharField(choices=paises,
                            max_length=50,
                            null=True,
                            blank=True)
    avatar = models.ForeignKey(Avatar,
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)

    def texto_ranking(self):
        return self.RANKINGS[self.ranking]

    @property
    def ranking(self):
        cantPosts = self.posts.count()
        cantLikes = self.likes.count()
        cantComentarios = self.comentarios.count()

        if (cantComentarios >= 1 and cantPosts >= 1 and cantLikes >= 1):
            if (cantComentarios < 3 or cantPosts < 3 or cantLikes < 3):
                return 1
            else:
                if (cantComentarios < 5 or cantPosts < 5 or cantLikes < 5):
                    return 2
                else:
                    return 3
        else:
            return 0
