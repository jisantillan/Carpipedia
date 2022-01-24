# Generated by Django 3.2.8 on 2021-11-11 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_carga_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_hijos', to='posts.comentario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='cuerpo',
            field=models.TextField(verbose_name='Escribir un comentario...'),
        ),
        migrations.AlterField(
            model_name='post',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
