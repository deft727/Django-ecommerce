# Generated by Django 3.0.8 on 2021-01-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20210124_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='адресс Фейсбук'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='facebooktitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' Название страницы Фейсбук'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='instatitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' Название страницы Инстаграмм'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='insta',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='адресс Инстаграмм'),
        ),
    ]
