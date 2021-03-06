# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0004_auto_20180517_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='damage_grade',
            field=models.CharField(choices=[(b'NONE', b'NONE'), (b'LIGHT', b'LIGHT'), (b'SEVERE', b'SEVERE'), (b'DEVASTATING', b'DEVASTATING')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='is_damaged',
            field=models.CharField(choices=[(b'LEAKING', b'LEAKING'), (b'NOT LEAKING', b'NOT LEAKING')], default='NOT Leaking', max_length=100),
        ),
    ]
