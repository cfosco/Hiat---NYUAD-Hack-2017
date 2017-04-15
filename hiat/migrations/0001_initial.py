# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 09:13
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.TextField(default=b'')),
                ('description', models.TextField(default=b'')),
                ('date_time', models.DateTimeField()),
                ('wage', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('category', models.TextField(default=b'')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=b'')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(default=b'')),
                ('last_name', models.TextField(default=b'')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('credit', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('skills', models.TextField(default=b'')),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiat.JobVendor'),
        ),
    ]