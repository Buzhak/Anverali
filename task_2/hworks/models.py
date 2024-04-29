from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class BaseModel(models.Model):
    title = models.CharField('Название',max_length=200)


    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Group(BaseModel):
    description = models.TextField('Описание группы')
    

class Hwork(BaseModel):
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Стоимость')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Пользователь'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='%(class)ss',
        blank=True,
        null=True,
        verbose_name='Группа'
    )


class Order(BaseModel):
    description = models.TextField('Описание')
    start_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField('Стоимость')
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Заказчик'
    )
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
