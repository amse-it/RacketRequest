# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('receiver_visible', models.BooleanField(default=True)),
                ('sender_visible', models.BooleanField(default=True)),
                ('receiver', models.ForeignKey(related_name='messages_received', default=None, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='messages_sent', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(to='messaging.Thread'),
        ),
    ]
