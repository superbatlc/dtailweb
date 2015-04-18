# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonegroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('code', models.CharField(max_length=10, verbose_name=b'Codice')),
                ('parent', models.ForeignKey(related_name='child_phonegroup_set', blank=True, to='phonegroups.Phonegroup', help_text=b'The father of this group', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhonegroupCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call', models.ForeignKey(to='calls.Call')),
                ('phonegroup', models.ForeignKey(to='phonegroups.Phonegroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhonegroupExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extension', models.CharField(max_length=4)),
                ('phonegroup', models.ForeignKey(to='phonegroups.Phonegroup')),
                ('system', models.ForeignKey(to='systems.System')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
