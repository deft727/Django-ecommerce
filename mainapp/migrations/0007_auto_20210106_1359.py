# Generated by Django 3.0.8 on 2021-01-06 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210106_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changemyinfo',
            old_name='Adress1',
            new_name='adress1',
        ),
        migrations.RenameField(
            model_name='changemyinfo',
            old_name='Adress2',
            new_name='adress2',
        ),
    ]
