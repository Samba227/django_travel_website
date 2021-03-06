# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-21 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190721_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Web',
            },
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]
