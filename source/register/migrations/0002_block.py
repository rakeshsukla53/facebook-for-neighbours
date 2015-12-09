# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('bid', models.IntegerField(serialize=False, primary_key=True)),
                ('bname', models.CharField(max_length=100)),
                ('hid', models.ForeignKey(to='register.Hood')),
            ],
        ),
    ]
