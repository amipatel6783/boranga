# Generated by Django 3.2.12 on 2022-06-22 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0018_communitylogdocument_communitylogentry_specieslogdocument_specieslogentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conservationattributes',
            name='species',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='species_conservation_attributes', serialize=False, to='boranga.species'),
        ),
    ]
