# Generated by Django 2.2.13 on 2023-06-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0040_auto_20230606_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='is_adjudication',
            field=models.BooleanField(default=False, null=True),
        ),
    ]