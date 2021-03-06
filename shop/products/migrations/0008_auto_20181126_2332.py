# Generated by Django 2.0.2 on 2018-11-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181126_2014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trademark',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='trademark',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]
