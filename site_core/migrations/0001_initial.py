# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(choices=[(0, b'Request'), (1, b'Racket')])),
                ('category_id', models.IntegerField()),
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
                ('racket', models.ForeignKey(to='site_core.Racket')),
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
                ('category', models.IntegerField(choices=[(0, b'Request'), (1, b'Racket')])),
                ('category_id', models.IntegerField()),
                ('path', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, b'Video'), (1, b'Audio'), (2, b'Image'), (3, b'Text')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birthday', models.DateField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reputation',
            name='referral',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reputation',
            name='user',
            field=models.ForeignKey(related_name='reputations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='racket',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='racket',
            name='request',
            field=models.ForeignKey(to='site_core.Request'),
        ),
    ]
