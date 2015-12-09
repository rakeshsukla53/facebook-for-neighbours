# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_thread'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('mtext', models.TextField()),
                ('mauthor', models.ForeignKey(to='register.Registration')),
                ('tid', models.ForeignKey(to='register.Thread')),
            ],
        ),
    ]
