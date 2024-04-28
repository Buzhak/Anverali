# Generated by Django 5.0.4 on 2024-04-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_hworksuser_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hworksuser',
            name='exp',
            field=models.TextField(blank=True, help_text='Расскажите о вашем опыте рабрты', null=True, verbose_name='Ваш опыт работы'),
        ),
        migrations.AlterField(
            model_name='hworksuser',
            name='is_freelancer',
            field=models.BooleanField(default=False, help_text='Если вы покупатель, оставьте это поле пустым', verbose_name='Я продавец'),
        ),
    ]
