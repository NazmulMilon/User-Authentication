# Generated by Django 3.2.6 on 2021-08-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_img_mainuser_imgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainuser',
            name='imgs',
        ),
        migrations.AddField(
            model_name='mainuser',
            name='images',
            field=models.ImageField(blank=True, upload_to='main'),
        ),
    ]
