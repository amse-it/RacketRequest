# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_core', '0002_auto_20150629_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
