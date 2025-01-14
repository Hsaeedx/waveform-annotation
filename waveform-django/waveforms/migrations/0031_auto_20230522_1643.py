# Generated by Django 2.2.13 on 2023-05-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0030_auto_20230117_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaveformEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50)),
                ('record', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='waveforms',
            field=models.ManyToManyField(related_name='annotators', to='waveforms.WaveformEvent'),
        ),
    ]
