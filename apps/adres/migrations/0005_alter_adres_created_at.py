# Generated by Django 4.2 on 2024-01-12 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adres', '0004_alter_adres_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 20, 47, 51, 679308), editable=False),
        ),
    ]
