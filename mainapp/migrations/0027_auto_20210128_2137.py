# Generated by Django 3.0.8 on 2021-01-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20210124_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytopimage',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/TopImage/', verbose_name='Изображение 1'),
        ),
    ]
