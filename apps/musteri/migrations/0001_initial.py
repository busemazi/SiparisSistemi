# Generated by Django 4.2 on 2023-12-23 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=255)),
                ('soyad', models.CharField(max_length=255)),
                ('cinsiyet', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 23, 10, 38, 53, 257995), editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'musteri',
            },
        ),
    ]
