# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20170721_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artiste'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'réservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'prospect'},
        ),
        migrations.AlterModelOptions(
            name='disk',
            options={'verbose_name': 'disque'},
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='Demande traitée'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Demande effectuée le'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activé'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='disks', to='manager.Artist'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='reference',
            field=models.IntegerField(verbose_name='référence'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titre'),
        ),
    ]