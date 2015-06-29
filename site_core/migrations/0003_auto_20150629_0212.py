# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('site_core', '0002_auto_20150629_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
