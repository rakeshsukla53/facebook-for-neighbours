# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=100)),
                ('upassword', models.CharField(max_length=100)),
                ('uphone', models.IntegerField(null=True, blank=True)),
                ('uemail', models.EmailField(default=b'rrs402@nyu.edu', max_length=254)),
                ('uintro', models.TextField(null=True, blank=True)),
                ('uphoto', models.ImageField(default=b'static/img/natural_join_is_inner_join.png', upload_to=b'')),
                ('uhood', models.CharField(max_length=10, null=True)),
                ('uaddress', models.CharField(default=b'ABC', max_length=100)),
                ('uhid', models.ForeignKey(to='register.Hood')),
            ],
        ),
    ]
