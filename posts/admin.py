from django.contrib import admin
from .models import Post, Categoria, Comentario

# Register your models here.
admin.site.register(Post)
admin.site.register(Categoria)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('cuerpo', 'post', 'hora_creacion', 'user')
    list_filter = ('hora_creacion', )
    search_fields = ('cuerpo', )