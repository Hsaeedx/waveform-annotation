# Generated by Django 2.2.13 on 2021-08-02 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0010_auto_20210802_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='when_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
