from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    POS = [
        ('A', 'Админ'),
        ('M', 'Менеджер'),
        ('S', 'Продавец'),
        ('C', 'Клиент'),
    ]

    class Meta:
        db_table = 'my_user'
        verbose_name = 'Пользовател'
        verbose_name_plural = 'Пользователи'

    image = models.ImageField(verbose_name='Фото', upload_to='Customers/%Y/%m/%d', blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=20, choices=POS)

    def __str__(self):
        return f'{self.username}'




class Customer(models.Model):
    pass
