# Generated by Django 2.2.14 on 2020-07-27 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autropolis_map', '0006_local_overrider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='super',
            options={'ordering': ['team', 'nome']},
        ),
    ]
