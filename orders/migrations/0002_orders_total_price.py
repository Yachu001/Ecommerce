# Generated by Django 5.1.1 on 2024-10-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
