from django.db import models
from django.contrib.auth.models import AbstractUser


class HworksUser(AbstractUser):
    '''
    Класс расширяет стандарного юзера джанги
    '''
    exp = models.TextField('Ваш опыт работы', blank=True, null=True)
    is_freelancer = models.BooleanField(default=False)
