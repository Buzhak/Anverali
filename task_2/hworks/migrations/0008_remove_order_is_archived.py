# Generated by Django 5.0.4 on 2024-04-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hworks', '0007_hwork_is_archived_order_is_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_archived',
        ),
    ]
