from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):

    title = models.CharField('Название группы',max_length=200)
    description = models.TextField('Описание группы')

    def __str__(self):
        return self.title
    

class Hwork(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Стоимость')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='%(class)ss',
        blank=True,
        null=True,
        verbose_name="Группа"
    )

    def __str__(self):
        return self.text