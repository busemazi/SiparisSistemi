# Generated by Django 4.2 on 2023-12-23 10:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('urun', '0001_initial'),
        ('siparis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrunSiparis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adet', models.IntegerField(default=0)),
                ('fiyat', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 23, 10, 38, 53, 259397), editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('siparis_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='siparis.siparis')),
                ('urun_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='urun.urun')),
            ],
            options={
                'db_table': 'urun_siparis',
            },
        ),
    ]