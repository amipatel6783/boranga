# Generated by Django 3.2.20 on 2023-09-19 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0173_auto_20230913_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalobservation',
            name='alive_adult',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='alive_juvenile',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='alive_pouch_young',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='alive_unsure',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='dead_adult',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='dead_juvenile',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='dead_pouch_young',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='animalobservation',
            name='dead_unsure',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
