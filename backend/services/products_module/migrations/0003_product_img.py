# Generated by Django 4.1.1 on 2023-02-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.TextField(max_length=2000, null=True, verbose_name='img'),
        ),
    ]
