# Generated by Django 3.2.6 on 2021-08-20 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_mainuser_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='imgs',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='main'),
            preserve_default=False,
        ),
    ]