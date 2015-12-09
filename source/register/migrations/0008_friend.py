# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_history_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('fuid1', models.ForeignKey(to='register.Registration')),
                ('fuid2', models.ForeignKey(related_name='+', to='register.Registration')),
                ('hid', models.ForeignKey(to='register.Hood')),
            ],
        ),
    ]
