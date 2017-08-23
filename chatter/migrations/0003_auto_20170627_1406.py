# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0002_chat_name_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='data_type',
            field=models.CharField(max_length=20, default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='parent',
            field=models.CharField(max_length=20, default='none'),
            preserve_default=False,
        ),
    ]
