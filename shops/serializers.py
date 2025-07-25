from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shops.models import Contacts, Product, Factory, RetailNetwork, IndividualEntrepreneur


class ContactsSerializer(ModelSerializer):
    """Сериализатор для моделей контактов."""
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    """Сериализатор для моделей продуктов."""
    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(ModelSerializer):
    """Сериализатор для моделей заводов."""
    class Meta:
        model = Factory
        fields = '__all__'


class RetailNetworkSerializer(ModelSerializer):
    """Сериализатор для моделей розничных сетей, кроме обновления."""
    class Meta:
        model = RetailNetwork
        fields = '__all__'


class RetailNetworkUpdateSerializer(ModelSerializer):
    """Сериализатор для обновления моделей розничных сетей(поле задолженность перед поставщиком недоступно для
    изменения)."""
    class Meta:
        model = RetailNetwork
        exclude = ('debt_to_supplier',)


class IndividualEntrepreneurSerializer(ModelSerializer):
    """Сериализатор для моделей индивидуальных предпринимателей, кроме обновления."""
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'

    def validate(self, data):
        """Проверка, что только у модели есть только 1 поставщик"""
        if 'provider_factory' in data and 'provider_retail_network' in data:
            raise serializers.ValidationError("Может быть не более одного поставщика.")
        return data


class IndividualEntrepreneurUpdateSerializer(ModelSerializer):
    """Сериализатор для обновления моделей индивидуальных предпринимателей."""
    class Meta:
        model = IndividualEntrepreneur
        exclude = ('debt_to_supplier',)