from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Customer(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    surname = models.CharField(max_length=80, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0, blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='Customers/%Y/%m/%d', blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=80)

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        unique_together = ['name', 'surname']


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='О категория')
    is_active = models.BooleanField(verbose_name='Подтверждённый', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    title = models.CharField(max_length=80, verbose_name='Название')
    is_active = models.BooleanField(verbose_name='Подтверждённый', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Под-категория'
        verbose_name_plural = 'Под-категории'


class Product(models.Model):
    MEN_WOMAN = [
        ('M', 'Мужской'),
        ('W', 'Женский'),
    ]
    COM = 'COM'
    USD = 'USD'
    RUB = 'RUB'
    C_U_R = [
        ('COM', 'сом'),
        ('USD', 'доллар'),
        ('RUB', 'руб'),
    ]
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    sub_category = ChainedForeignKey(SubCategory, chained_field='category', chained_model_field='category',
                                     show_all=False,
                                     auto_choose=True,
                                     sort=True, verbose_name='Под-категория')
    title = models.CharField(max_length=80, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото', upload_to='Product/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание')
    gender = models.CharField(verbose_name='Пол', choices=MEN_WOMAN, null=True, blank=True, max_length=1)
    is_popular = models.BooleanField(verbose_name='Популярный?', default=True, null=True)
    amount = models.PositiveIntegerField(verbose_name='Кол-во', default=1)
    article = models.BigIntegerField(verbose_name='Артикл', unique=True, null=True)
    old_price = models.PositiveIntegerField(verbose_name='Старая цена', default=0)
    cur = models.CharField(verbose_name='Волюта', choices=C_U_R, default='C', max_length=3)
    new_price = models.IntegerField(verbose_name='Новая цена', null=True, blank=True)
    pub_date = models.DateField(verbose_name='Дата публикации', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title}---{self.sub_category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    FEE = [
        ('CASH', 'Наличка'),
        ('CARD', 'Карта'),
    ]
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    fee = models.CharField(verbose_name='Платеж', choices=FEE, default='CARD', max_length=4)
    service = models.BooleanField(verbose_name='Доставка', default=True)
    address = models.CharField(verbose_name='Адрес', max_length=80)
    total_item = models.PositiveIntegerField(verbose_name='Кол-во', default=1)

    ord_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        # unique_together = ['customer']


class ItemOrders(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, null=True, verbose_name='Продукт')
    quantity = models.IntegerField(verbose_name='Кол-во', default=1)
    color = models.CharField(verbose_name='Цвет', max_length=20)
    order = models.ForeignKey(Order, models.SET_NULL, null=True, blank=True, verbose_name='Заказчик')

    def __str__(self):
        return f'{self.order}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
