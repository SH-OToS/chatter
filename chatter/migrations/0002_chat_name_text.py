# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name_text',
            field=models.CharField(max_length=100, default=datetime.datetime(2017, 6, 25, 12, 38, 20, 472508, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
