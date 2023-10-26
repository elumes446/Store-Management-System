# Generated by Django 4.2.4 on 2023-08-25 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_product_factory_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_receive_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]