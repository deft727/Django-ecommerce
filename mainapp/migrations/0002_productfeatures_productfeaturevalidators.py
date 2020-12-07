# Generated by Django 3.0.8 on 2020-12-02 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_key', models.CharField(max_length=100, verbose_name='Ключ характеристики')),
                ('feature_name', models.CharField(max_length=255, verbose_name='Наименование характеристики')),
                ('postfix_for_value', models.CharField(blank=True, help_text='Для хар-к можно добавить постфикс', max_length=25, null=True, verbose_name='Постфикс для значения')),
                ('use_in_filter', models.CharField(default=False, max_length=50, verbose_name='Использовать фильтрацию товаров на странице')),
                ('filter_type', models.CharField(choices=[('radio', 'Радиокнопка'), ('checkbox', 'Чекбокс')], default='checkbox', max_length=20, verbose_name='Тип фильтра')),
                ('filter_measures', models.CharField(help_text='Единица измерения для фильтра', max_length=50, verbose_name='Единица измерения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeatureValidators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_value', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Значение хар-ки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
                ('feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductFeatures', verbose_name='Характеристика')),
            ],
        ),
    ]
