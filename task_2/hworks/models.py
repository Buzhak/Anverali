from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    title = models.CharField('Название', max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Group(BaseModel):
    description = models.CharField('Описание группы', max_length=200)

    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группы'


class Hwork(BaseModel):
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Стоимость')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Продавец'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='%(class)ss',
        blank=True,
        null=True,
        verbose_name='Группа'
    )
    is_archived = models.BooleanField('Hwork в архиве', default=False)

    class Meta:
        verbose_name = 'Хворк'
        verbose_name_plural = 'Хворки'


class Order(BaseModel):
    description = models.TextField(
        verbose_name='Техническое задание',
        help_text='Опишите техническое задание как можно подробнее'
    )
    start_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField('Стоимость')
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Заказчик'
    )
    seller = models.CharField('Продавец', max_length=100)
    hwork = models.ForeignKey(
        Hwork,
        on_delete=models.SET_NULL,
        related_name='%(class)ss',
        blank=True,
        null=True,
        verbose_name='Hwork'
    )
    is_ready = models.BooleanField(verbose_name='Заказ сделан', default=False)
    is_finished = models.BooleanField(verbose_name='Заказ закрыт', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
