# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20151128_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(to='register.Registration')),
            ],
        ),
    ]
