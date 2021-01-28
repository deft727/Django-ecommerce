# Generated by Django 3.0.8 on 2021-01-12 17:35

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210111_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='mainapp.Category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='mainapp.Category', verbose_name='Выберите категорию'),
        ),
    ]