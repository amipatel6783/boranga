# Generated by Django 3.2.20 on 2023-08-03 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0154_auto_20230803_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speciesconservationattributes',
            old_name='flowering_period',
            new_name='flowering_period_id',
        ),
        migrations.RenameField(
            model_name='speciesconservationattributes',
            old_name='fruiting_period',
            new_name='fruiting_period_id',
        ),
    ]
