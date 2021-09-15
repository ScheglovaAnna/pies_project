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

class Pies(models.Model):
    pies_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image_pies = models.ImageField(verbose_name="Картинка тортика")
    price = models.CharField(max_length=50, blank=True, null=True)
    sale_price = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    information_2 = models.TextField(blank=True, null=True)
    # quantity - количество пирожков;

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


class Basket(models.Model):
    pies_basket = models.ManyToManyField(Pies, blank=True, verbose_name="Тортики в корзине",
                                  related_name="basket_pies")
    owner = models.ForeignKey('User', verbose_name="Покупатель", on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=9, verbose_name="Общая цена", decimal_places=2)
    quantity = models.CharField(max_length=100, verbose_name="Колличество", null=True)


class Order(models.Model):
    """Заказ пользователя"""

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ находится в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ получен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    #user = models.ForeignKey('User', verbose_name="Покупатель", related_name="orders", on_delete=models.CASCADE)
    buying_type = models.CharField(max_length=100, verbose_name='выбор доставки', choices=BUYING_TYPE_CHOICES)
    status_type = models.CharField(max_length=100, verbose_name='статус доставки', choices=STATUS_CHOICES, null=True)
    basket = models.ForeignKey('Basket', verbose_name="корзина", related_name="basket", on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий к заказу')
    date_create = models.DateField(verbose_name='Дата создания заказа', auto_now=True)
    data_order = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)
    #pies = models.ManyToManyField(Pies, verbose_name="Тортики", blank=True)

# class Payment(models.Model):