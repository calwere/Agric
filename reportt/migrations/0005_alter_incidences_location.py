# Generated by Django 4.1.7 on 2023-02-17 16:29

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportt', '0004_alter_incidences_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidences',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(max_length=4326, srid=4326),
        ),
    ]