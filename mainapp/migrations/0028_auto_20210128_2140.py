# Generated by Django 3.0.8 on 2021-01-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20210128_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/AboutImage/', verbose_name='Изображение '),
        ),
        migrations.AlterField(
            model_name='logo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/Logo', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='myimage',
            name='imagedown1',
            field=models.ImageField(blank=True, null=True, upload_to='images/DownImage', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='myimage',
            name='imagedown2',
            field=models.ImageField(blank=True, null=True, upload_to='images/DownImage', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='mytopimage',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/TopImage/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='images/photos/%Y/%m/%d/', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/%Y/%m/%d/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/%Y/%m/%d/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/%Y/%m/%d/', verbose_name='Изображение 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/%Y/%m/%d/', verbose_name='Изображение 5'),
        ),
    ]