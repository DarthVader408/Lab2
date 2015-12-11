# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcard', models.IntegerField()),
                ('valid', models.BooleanField()),
                ('data2', models.DateField()),
                ('nomer_oper', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomer_id', models.IntegerField()),
                ('familia', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('otchestvo', models.CharField(max_length=30)),
                ('pol', models.CharField(max_length=7)),
                ('data', models.DateField()),
                ('mobile', models.IntegerField()),
                ('nomer_dogovora', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dogov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uslov', models.TextField()),
                ('data1', models.DateField()),
                ('idcard', models.IntegerField()),
                ('iddog', models.ForeignKey(to='Purple.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Oper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomer_oper', models.IntegerField()),
                ('opera', models.TextField()),
                ('data3', models.DateField()),
            ],
        ),
    ]
