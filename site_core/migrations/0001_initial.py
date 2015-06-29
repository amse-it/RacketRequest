# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(default=None)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Racket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_started', models.DateField()),
                ('created', models.DateField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reputation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_credible', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duration', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(default=None)),
                ('path', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, b'Video'), (1, b'Audio'), (2, b'Image'), (3, b'Text')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(default=None, to='contenttypes.ContentType')),
            ],
        ),
    ]
