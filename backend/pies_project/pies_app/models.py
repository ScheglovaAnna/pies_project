from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=25)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'telephone_number']


class Order(models.Model):
    """Бронирование, Заказ"""
    buying_types = (
        ('s', 'Самовывоз'),
        ('d', 'Доставка'),
    )
    status_types = (
        ('n', 'Новый заказ'),
        ('in', 'Заказ находится в обработке'),
        ('is', 'Заказ готов'),
        ('c', 'Заказ получен'),
    )
    order = models.AutoField(primary_key=True)

    owner = models.ForeignKey('User', verbose_name="Покупатель", on_delete=models.CASCADE, null=True)
    final_price = models.DecimalField(max_digits=9, verbose_name="Общая цена", decimal_places=2, null=True)
    quantity = models.CharField(max_length=100, verbose_name="Количество", null=True)
    date_create = models.DateField(verbose_name='Дата создания заказа', auto_now=True)
    data_order = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=status_types, null=True)
    buying = models.CharField(max_length=100, verbose_name='Статус доставки', choices=buying_types,
                                   null=True, default='n')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий к заказу')
    pies_id = models.ForeignKey('Pies', on_delete=models.CASCADE, null=True, related_name='pies_id_fk',
                                    verbose_name='Pies')


class Pies(models.Model):
    pies_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image_pies = models.ImageField(verbose_name="Картинка тортика")
    price = models.CharField(max_length=50, blank=True, null=True)
    sale_price = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    information_2 = models.TextField(blank=True, null=True)
    produser_types = (
        ('r', 'Россия'),
        ('i', 'Италия'),
        ('p', 'Польша'),
        ('f', 'Франция'),
        ('b', 'Бельгия'),
    )
    produser = models.CharField(choices=produser_types, max_length=20)
    have_types = (
        ('s', 'нет в наличии'),
        ('m', 'мало в наличии'),
        ('l', 'много в наличии'),
    )
    have = models.CharField(choices=have_types, max_length=20)


# class Order(models.Model):
#     """Заказ пользователя"""
