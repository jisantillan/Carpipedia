# Generated by Django 3.2.9 on 2021-11-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='nivel',
            field=models.IntegerField(choices=[(0, 'sin premium'), (1, 'premium basico'), (2, 'premium medio'), (3, 'premium avanzado')], default=0),
        ),
    ]
