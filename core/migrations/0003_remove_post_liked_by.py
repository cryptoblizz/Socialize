# Generated by Django 2.1.4 on 2019-01-24 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by',
        ),
    ]