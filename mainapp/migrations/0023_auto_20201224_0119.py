# Generated by Django 3.0.8 on 2020-12-23 23:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20201223_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='characteristics',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
