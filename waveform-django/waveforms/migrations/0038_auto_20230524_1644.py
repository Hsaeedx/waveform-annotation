# Generated by Django 2.2.13 on 2023-05-24 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0037_auto_20230524_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waveformevent',
            options={'ordering': ['project', 'record', 'event']},
        ),
    ]
