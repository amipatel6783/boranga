# Generated by Django 3.2.12 on 2022-06-15 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0016_auto_20220610_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conservationthreat',
            name='document',
        ),
        migrations.RemoveField(
            model_name='conservationthreat',
            name='source',
        ),
        migrations.RemoveField(
            model_name='conservationthreat',
            name='threat_description',
        ),
        migrations.AddField(
            model_name='conservationthreat',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_threats', to='boranga.community'),
        ),
        migrations.AddField(
            model_name='conservationthreat',
            name='date_observed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conservationthreat',
            name='threat_agent',
            field=models.CharField(default='None', max_length=512),
        ),
        migrations.AlterField(
            model_name='conservationthreat',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='species_threats', to='boranga.species'),
        ),
    ]
