# Generated by Django 2.2 on 2022-03-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='updated_at',
            field=models.TimeField(auto_now=True),
        ),
    ]