# Generated by Django 2.2.14 on 2020-07-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autropolis_map', '0002_local_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='especial',
            field=models.CharField(default='', max_length=200),
        ),
    ]
