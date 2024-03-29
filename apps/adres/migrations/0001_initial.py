# Generated by Django 4.2 on 2023-12-23 10:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musteri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sehir', models.CharField(max_length=255)),
                ('ilce', models.CharField(max_length=255)),
                ('aciklama', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 23, 10, 38, 53, 258130), editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('musteri_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='musteri.musteri')),
            ],
            options={
                'db_table': 'adres',
            },
        ),
    ]
