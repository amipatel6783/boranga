# Generated by Django 3.2.20 on 2023-08-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0159_auto_20230809_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciesconservationattributes',
            name='minimum_fire_interval_choice',
            field=models.CharField(blank=True, choices=[(1, 'years'), (2, 'months')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='speciesconservationattributes',
            name='minimum_fire_interval_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='speciesconservationattributes',
            name='minimum_fire_interval_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
