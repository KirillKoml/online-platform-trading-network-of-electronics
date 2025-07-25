import django_filters

from shops.models import Factory, RetailNetwork, IndividualEntrepreneur


class FactoryFilter(django_filters.FilterSet):
    """Фильтр для FactoryListAPIView, чтобы была сортировка по странам."""
    country = django_filters.CharFilter(field_name='contacts__country')

    class Meta:
        model = Factory
        fields = ['country']


class RetailNetworkFilter(django_filters.FilterSet):
    """Фильтр для RetailNetworkListAPIView, чтобы была сортировка по странам."""
    country = django_filters.CharFilter(field_name='contacts__country')

    class Meta:
        model = RetailNetwork
        fields = ['country']


class IndividualEntrepreneurFilter(django_filters.FilterSet):
    """Фильтр для IndividualEntrepreneurListAPIView, чтобы была сортировка по странам."""
    country = django_filters.CharFilter(field_name='contacts__country')

    class Meta:
        model = IndividualEntrepreneur
        fields = ['country']