# Generated by Django 2.2.7 on 2019-12-01 18:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitchens', '0005_auto_20191122_0315'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Kitchen',
        ),
    ]