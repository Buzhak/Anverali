# Generated by Django 5.0.4 on 2024-04-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hworks', '0005_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
