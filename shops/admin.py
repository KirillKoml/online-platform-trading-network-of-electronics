from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin.filters import SimpleListFilter
from django.utils.translation import gettext_lazy as _

from shops.models import Contacts, Product, Factory, RetailNetwork, IndividualEntrepreneur


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Админка для контактов."""
    list_display = ('id', 'title', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для продуктов."""
    list_display = ('id', 'title')


class CityFactoryFilter(SimpleListFilter):
    """Фильтрация по городу для заводов."""
    title = _('Город')  # Название фильтра в админке
    parameter_name = 'city'  # Имя параметра URL для фильтрации

    def lookups(self, request, model_admin):
        """Выполняю генерацию списка значений, по которым можно будет фильтровать"""
        cities = set([factory.contacts.city for factory in Factory.objects.all()])
        return [(city, city) for city in sorted(cities)]

    def queryset(self, request, queryset):
        """Метод queryset отвечает за применение фильтра к запросу"""
        if self.value():
            return queryset.filter(contacts__in=Contacts.objects.filter(city=self.value()))
        else:
            return queryset



@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """Админка для завода с фильтрацией по городу."""
    list_display = ('id', 'title')
    list_filter = [CityFactoryFilter]


class CityRetailNetworkFilter(SimpleListFilter):
    """Фильтрация по городу для розничных сетей."""
    title = _('Город')  # Название фильтра в админке
    parameter_name = 'city'  # Имя параметра URL для фильтрации

    def lookups(self, request, model_admin):
        """Выполняю генерацию списка значений, по которым можно будет фильтровать"""
        cities = set([retail_network.contacts.city for retail_network in RetailNetwork.objects.all()])
        return [(city, city) for city in sorted(cities)]

    def queryset(self, request, queryset):
        """Метод queryset отвечает за применение фильтра к запросу"""
        if self.value():
            return queryset.filter(contacts__in=Contacts.objects.filter(city=self.value()))
        else:
            return queryset


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    """Админка для розничной сети со ссылкой на поставщика и admin action по очищению задолженности перед поставщиком."""
    list_display = ('id', 'title', 'link_to_supplier')
    list_filter = [CityRetailNetworkFilter]
    actions = ('debt_cancellation',)

    @admin.display(description='Поставщик')
    def link_to_supplier(self, obj):
        """Метод для получения ссылки на поставщика"""
        if obj.provider:
            return format_html(
                f'<a href="/admin/shops/factory/{obj.provider.id}/change/">{obj.provider.title}')
        return 'не указан'

    def debt_cancellation(modeladmin, request, queryset):
        """Admin action по очищению задолженности перед поставщиком у выбранных моделей"""
        queryset.update(debt_to_supplier=0)


class IndividualEntrepreneurFilter(SimpleListFilter):
    """Фильтрация по городу для ИП."""
    title = _('Город')  # Название фильтра в админке
    parameter_name = 'city'  # Имя параметра URL для фильтрации

    def lookups(self, request, model_admin):
        """Выполняю генерацию списка значений, по которым можно будет фильтровать"""
        cities = set([individual_entrepreneur.contacts.city for individual_entrepreneur in IndividualEntrepreneur.objects.all()])
        return [(city, city) for city in sorted(cities)]

    def queryset(self, request, queryset):
        """Метод queryset отвечает за применение фильтра к запросу"""
        if self.value():
            return queryset.filter(contacts__in=Contacts.objects.filter(city=self.value()))
        else:
            return queryset


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    """Админка для индивидуального предпринимателя со ссылкой на поставщика, фильтрацией по городу и admin action по
    очищению задолженности перед поставщиком."""
    list_display = ('id', 'title', 'linked_factory')
    list_filter = [IndividualEntrepreneurFilter]
    actions = ('debt_cancellation',)

    @admin.display(description='Поставщик')
    def linked_factory(self, obj):
        """Метод для получения ссылки на поставщика"""
        if obj.provider_factory:
            return format_html(f'<a href="/admin/shops/factory/{obj.provider_factory.id}/change/">{obj.provider_factory.title}')
        elif obj.provider_retail_network:
            return format_html(f'<a href="/admin/shops/retailnetwork/{obj.provider_retail_network.id}/change/">{obj.provider_retail_network.title}')
        return 'не указан'

    def debt_cancellation(modeladmin, request, queryset):
        """Admin action по очищению задолженности перед поставщиком у выбранных моделей"""
        queryset.update(debt_to_supplier=0)