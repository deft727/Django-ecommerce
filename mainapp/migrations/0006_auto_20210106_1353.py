# Generated by Django 3.0.8 on 2021-01-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210105_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeMyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toptext', models.CharField(blank=True, max_length=150, null=True, verbose_name='Текст в левом углу')),
                ('Adress1', models.CharField(blank=True, max_length=150, null=True, verbose_name='Адресс 1')),
                ('street1', models.CharField(blank=True, max_length=150, null=True, verbose_name='Улица для адресс 1')),
                ('email1', models.EmailField(blank=True, max_length=150, null=True, verbose_name='емайл для адрес 1')),
                ('Adress2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Адресс 2')),
                ('street2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Улица для адресс 2')),
                ('email2', models.EmailField(blank=True, max_length=150, null=True, verbose_name='емайл для адрес 2')),
                ('about', models.CharField(blank=True, max_length=150, null=True, verbose_name='Пару слов о сайте')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='mytopimage',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='TopImage/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='mytopimage',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='TopImage/', verbose_name='Изображение 2'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
    ]