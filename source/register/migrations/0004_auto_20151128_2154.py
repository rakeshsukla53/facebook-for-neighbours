# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='uphone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
