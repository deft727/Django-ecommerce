# Generated by Django 3.0.8 on 2020-12-22 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20201222_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='properties',
            new_name='characteristics',
        ),
    ]
