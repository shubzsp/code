# Generated by Django 2.2 on 2022-03-01 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_product_model'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_model',
        ),
    ]
