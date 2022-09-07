# Generated by Django 3.2.12 on 2022-09-01 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0070_auto_20220901_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conservationstatus',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conservation_status', to='boranga.community'),
        ),
        migrations.AlterField(
            model_name='conservationstatus',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conservation_status', to='boranga.species'),
        ),
    ]
