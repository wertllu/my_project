# Generated by Django 4.1.1 on 2023-02-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='send_push',
            field=models.BooleanField(default=True, verbose_name='endS Push'),
        ),
    ]
