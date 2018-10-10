# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-25 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crash', '0035_crash_decryption_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crash',
            name='decryption_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='encryption.DecryptionData'),
        ),
    ]
