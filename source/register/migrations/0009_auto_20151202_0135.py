# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_friend'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('fuid1', 'fuid2')]),
        ),
    ]
