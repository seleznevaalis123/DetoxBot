from django.db import models

class Users(models.Model):
    """Users"""

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    tg_id = models.BigIntegerField(verbose_name='tg id')
    tg_name = models.TextField(verbose_name='имя tg', null=True, blank=True, default='default')

    def __str__(self):
        return f'{self.tg_id, self.tg_name}'


class Category(models.Model):
    """Category"""
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category_name = models.CharField(verbose_name='Категория', max_length=250)
    category_desc = models.TextField(verbose_name='Описание категории', default='default', max_length=2000, null=True)
    category_photo = models.ImageField(upload_to='media/', verbose_name='Фото')

    def __str__(self):
        return f'{self.category_name}'


class TeaItems(models.Model):
    """TeaItems"""

    class Meta:
        db_table = 'tea_items'
        verbose_name = 'Чай и посуда'
        verbose_name_plural = 'Чай и посуда'

    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    item_name = models.CharField(verbose_name='Название', max_length=250)
    item_desc = models.TextField(verbose_name='Описание', max_length=2000)
    item_price_idr = models.FloatField(verbose_name='Цена в IDR', null=True, blank=True, default=0.000)
    item_price_thb = models.FloatField(verbose_name='Цена в THB', null=True, blank=True, default=0.000)
    item_price_aed = models.FloatField(verbose_name='Цена в AED', null=True, blank=True, default=0.000)
    item_price_rub = models.FloatField(verbose_name='Цена в RUB', null=True, blank=True, default=0.000)

    item_weight = models.CharField(verbose_name='Вес', null=True, blank=True, max_length=250)
    item_photo = models.ImageField(upload_to='media/', verbose_name='Фото')

    def __str__(self):
        return f'{self.item_name}'


class Cards(models.Model):
    """Cards"""

    class Meta:
        db_table = 'cards'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    tea_item = models.ForeignKey(TeaItems, on_delete=models.CASCADE, verbose_name='Название')
    item_price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_dt = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    currency = models.CharField(verbose_name='Валюта', max_length=250, null=True)

    def __str__(self):
        return f'{self.user, self.tea_item}'


'''class OrdersManager(models.Manager):
    pass'''


class Orders(models.Model):
    """Orders"""

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    Order_states = [
        ('NEW', 'новый'),
        ('IN_PROGRESS', 'в процессе'),
        ('DONE', 'исполнен'), ]

    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Юзер')
    created_dt = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)
    last_updated_dt = models.DateTimeField(verbose_name='Последнее обновление', auto_now=True, null=True, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=20, choices=Order_states)
    delivery_address = models.TextField(verbose_name='Адрес доставки', max_length=2000, null=True, blank=True)

    # objects = OrdersManager()

    def __str__(self):
        return f'{self.user}'


class OrderItems(models.Model):

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ', related_name='items')
    tea_item = models.ForeignKey(TeaItems, on_delete=models.CASCADE, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена', null=True, blank=True, default='0.000')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    currency = models.CharField(verbose_name='Валюта', max_length=250, null=True)

    def __str__(self):
        return f'{self.order}'


class Announcements(models.Model):
    """Announcements"""

    class Meta:
        db_table = 'announcements'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    announcement_desc = models.TextField(verbose_name='Описание', max_length=2000)
    item_photo = models.ImageField(upload_to='media/', verbose_name='Фото события')


# class Customer(models.Model, EmailSignalMixin):
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)
#
#     def customer_emails(self):
#         """Получатель - это клиент."""
#         return [self.email]
#
#     def management_mailing_list(self):
#         """Список получателей включает менеджеров."""
#         return ['selezneva.teset@gmail.com', 'seleznevaalis@gmail.com']

