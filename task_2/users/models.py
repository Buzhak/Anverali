from django.db import models
from django.contrib.auth.models import AbstractUser


class HworksUser(AbstractUser):
    '''
    Класс расширяет стандарного юзера джанги
    '''
    exp = models.TextField(
        'Ваш опыт работы',
        blank=True, null=True,
        help_text='Расскажите о вашем опыте рабрты'
    )
    is_freelancer = models.BooleanField(
        'Я продавец',
        default=False,
        help_text='Если вы покупатель, оставьте это поле пустым'
    )
