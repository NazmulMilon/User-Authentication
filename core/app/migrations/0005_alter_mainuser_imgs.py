# Generated by Django 3.2.6 on 2021-08-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_mainuser_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='imgs',
            field=models.ImageField(upload_to='media/image'),
        ),
    ]
