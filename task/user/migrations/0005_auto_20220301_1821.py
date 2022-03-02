# Generated by Django 2.2 on 2022-03-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_product_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('weight', models.CharField(max_length=100)),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post_model',
            options={'managed': False},
        ),
    ]