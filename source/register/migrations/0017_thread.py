# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20151202_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('tid', models.IntegerField(serialize=False, primary_key=True)),
                ('ttype', models.CharField(max_length=10, choices=[(b'HOOD', b'Hood'), (b'BLOCK', b'Block'), (b'FRIEND', b'Friend'), (b'NEIGHBOUR', b'Neighbour')])),
                ('tdate', models.DateTimeField(auto_now=True)),
                ('tdesc', models.TextField()),
                ('tauthor', models.ForeignKey(to='register.Registration')),
            ],
        ),
    ]
