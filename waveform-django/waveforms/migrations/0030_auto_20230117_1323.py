# Generated by Django 2.2.13 on 2023-01-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0029_auto_20230110_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='entrance_score',
            field=models.CharField(default='N/A', max_length=8),
        ),
    ]