# Generated by Django 3.1.14 on 2022-05-27 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20220527_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
