# Generated by Django 5.0 on 2023-12-09 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_content_slug_alter_content_introduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='slug',
        ),
    ]
