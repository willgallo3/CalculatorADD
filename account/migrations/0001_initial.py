# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-14 15:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc', models.PositiveIntegerField(default=0, verbose_name='BitCoin')),
                ('msc', models.PositiveIntegerField(default=0, verbose_name='maidsafecoin')),
                ('eth', models.PositiveIntegerField(default=0, verbose_name='Ethereum')),
                ('lit', models.PositiveIntegerField(default=0, verbose_name='Litecoin')),
                ('dol', models.PositiveIntegerField(default=0, verbose_name='Dollor')),
                ('ass', models.PositiveIntegerField(default=0, verbose_name='Asset')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
