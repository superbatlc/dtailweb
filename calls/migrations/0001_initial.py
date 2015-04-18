# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('system_id', models.IntegerField()),
                ('calldate', models.DateTimeField(verbose_name=b'Data chiamata')),
                ('trunk_src', models.CharField(max_length=10, verbose_name=b'Fascio Originante')),
                ('line_src', models.CharField(max_length=10, verbose_name=b'Linea Originante')),
                ('trunk_dst', models.CharField(max_length=10, verbose_name=b'Fascio Terminante')),
                ('line_dst', models.CharField(max_length=10, verbose_name=b'Linea Terminante')),
                ('src', models.CharField(max_length=80, verbose_name=b'Sorgente')),
                ('dst', models.CharField(max_length=80, verbose_name=b'Destinazione')),
                ('access_code', models.CharField(max_length=10, verbose_name=b'Codice Accesso')),
                ('duration', models.IntegerField(verbose_name=b'Durata')),
                ('billsec', models.IntegerField()),
                ('route', models.IntegerField()),
                ('calltype', models.IntegerField()),
                ('price', models.DecimalField(verbose_name=b'Prezzo', max_digits=7, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
