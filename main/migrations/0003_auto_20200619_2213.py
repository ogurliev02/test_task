# Generated by Django 3.0.7 on 2020-06-19 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_imagemodel_image_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='image_hash',
            new_name='url',
        ),
    ]