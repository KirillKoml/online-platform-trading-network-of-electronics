from django.core.validators import MinValueValidator
from django.db import models


class Contacts(models.Model):
    """Модель контактов."""
    title = models.CharField(max_length=75, verbose_name='Название фирмы')
    email = models.EmailField(unique=True, verbose_name='Почта фирмы')
    country = models.CharField(max_length=75, verbose_name='Страна фирмы')
    city = models.CharField(max_length=75, verbose_name='Город фирмы')
    street = models.CharField(max_length=75, verbose_name='Улица фирмы')
    house_number = models.PositiveIntegerField(verbose_name='Дом фирмы')

    class Meta:
        verbose_name = 'Контакты Фирмы'
        verbose_name_plural = 'Контакты фирмы'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    """Модель продукта."""
    title = models.CharField(max_length=75, verbose_name='Название')
    model = models.CharField(max_length=75, verbose_name='Модель')
    date_of_market_launch = models.DateField(verbose_name='дата выхода на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'


class Factory(models.Model):
    """Модель завода."""
    title = models.CharField(max_length=75, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты',
                                 related_name='factory_contacts')
    product = models.ManyToManyField(Product, verbose_name='Продукты', related_name='factory_Product', null=True,
                                     blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'{self.title}'


class RetailNetwork(models.Model):
    """Модель розничной сети."""
    title = models.CharField(max_length=75, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты',
                                 related_name='retail_network_contacts')
    product = models.ManyToManyField(Product, verbose_name='Продукты', related_name='retail_network_Product', null=True,
                                     blank=True)
    provider = models.ForeignKey(Factory, on_delete=models.SET_NULL, verbose_name='Поставщик', null=True, blank=True,
                                 related_name='retail_network_provider')
    debt_to_supplier = models.DecimalField(decimal_places=2,  validators=[MinValueValidator(0)], max_digits=13,
                                           verbose_name='Задолженность перед поставщиком с точностью до копеек')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return f'{self.title}'


class IndividualEntrepreneur(models.Model):
    """Модель индивидуального предпринимателя."""
    title = models.CharField(max_length=75, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты',
                                 related_name='individual_entrepreneur_contacts')
    product = models.ManyToManyField(Product, verbose_name='Продукты', related_name='individual_entrepreneur_Product',
                                     null=True, blank=True)
    provider_factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, verbose_name='Поставщик с завода',
                                 related_name='individual_entrepreneur_provider_factory', null=True, blank=True)
    provider_retail_network = models.ForeignKey(RetailNetwork, on_delete=models.SET_NULL, null=True, blank=True,
                                                verbose_name='Поставщик с розничной сети',
                                                related_name='individual_entrepreneur_provider_retail_network')
    debt_to_supplier = models.DecimalField(decimal_places=2,  validators=[MinValueValidator(0)], max_digits=13,
                                           verbose_name='Задолженность перед поставщиком с точностью до копеек')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return f'{self.title}'