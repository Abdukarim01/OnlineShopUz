# Generated by Django 3.2.9 on 2021-12-20 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211219_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discut',
            field=models.IntegerField(blank=True, default=0, verbose_name='Tovar chegirmasi'),
        ),
    ]