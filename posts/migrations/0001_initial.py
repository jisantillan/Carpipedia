# Generated by Django 3.2.7 on 2021-09-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('contenido', models.TextField(max_length=1000)),
                ('fecha_creacion', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]