# Generated by Django 3.2.6 on 2021-08-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210820_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='img',
            field=models.ImageField(blank=True, upload_to='main/'),
        ),
    ]
