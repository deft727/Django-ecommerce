# Generated by Django 3.0.8 on 2021-01-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20210124_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Информация на странице о Возврате',
                'verbose_name_plural': 'Информация на странице о Возврате',
            },
        ),
        migrations.RemoveField(
            model_name='returns',
            name='text',
        ),
        migrations.RemoveField(
            model_name='returns',
            name='title',
        ),
        migrations.AddField(
            model_name='returns',
            name='returns',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='returns',
            name='returnsText',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Дополнительный Текст'),
        ),
    ]
