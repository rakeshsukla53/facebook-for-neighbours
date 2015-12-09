# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20151201_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='session',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
