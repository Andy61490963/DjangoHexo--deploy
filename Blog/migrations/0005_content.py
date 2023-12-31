# Generated by Django 5.0 on 2023-12-08 14:19

import datetime
import django.db.models.deletion
import mdeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_homepost_introduction'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=20, verbose_name='Name')),
                ('introduction', mdeditor.fields.MDTextField(max_length=500, verbose_name='Introduction')),
                ('writer', models.CharField(max_length=20, null=True, verbose_name='writer')),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ownerid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='Blog.tag')),
            ],
        ),
    ]
