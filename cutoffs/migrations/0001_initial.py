# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=400)),
                ('total_branches', models.IntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=400, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('name', models.CharField(max_length=400, primary_key=True, serialize=False, unique=True)),
                ('region', models.CharField(blank=True, max_length=400, null=True)),
                ('total_institutions', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='University',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cutoffs.University'),
        ),
    ]
