# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_core', '0003_auto_20150629_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='duration',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
