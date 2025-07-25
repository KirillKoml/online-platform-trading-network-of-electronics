from rest_framework import serializers

from shops.models import IndividualEntrepreneur


class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = ['provider_factory', 'provider_retail_network']

    def validate(self, data):
        # Проверяем, что только одно из двух полей заполнено
        if ('provider_factory' in data and 'provider_retail_network' in data) or \
                (not 'provider_factory' in data and not 'provider_retail_network' in data):
            raise serializers.ValidationError("Только одно из полей должно быть заполнено.")

        return data