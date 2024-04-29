# Generated by Django 5.0.4 on 2024-04-28 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hworks', '0003_rename_author_hwork_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='hwork',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('is_ready', models.BooleanField(default=False, verbose_name='Заказ сделан')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Заказ закрыт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('hwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='hworks.hwork', verbose_name='Hwork')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
