# Generated by Django 3.1.14 on 2022-05-28 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_imagegallery_web_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='Address',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='location',
            name='post_date',
        ),
    ]
